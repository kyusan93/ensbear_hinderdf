@ECHO OFF
 
REM Disable UAC:
reg ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f
 
REM Disable recently accessed programs:
reg ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Start_TrackProgs /t REG_DWORD /d 0 /f
 
REM Disable recently accessed docs:
reg ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Start_TrackDocs /t REG_DWORD /d 0 /f
 
REM Disable recently added apps from start menu:
reg ADD "HKLM\Software\Policies\Microsoft\Windows\Explorer" /v HideRecentlyAddedApps /t REG_DWORD /d 1 /f
 
REM Disable last access:
fsutil behavior set disablelastaccess 1
 
REM Disable System Restore Point:
Reg ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v DisableSR /t REG_DWORD /d 1 /f
 
REM Disable Windows Error Reporting:
reg ADD "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting" /v Disabled /t REG_DWORD /d 1 /f
 
REM Disable Automatic Debugging for Application Crashes:
reg ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug Error Reporting" /v Disabled /t REG_DWORD /d 1 /f
 
REM Delete pagefile.sys:
wmic computersystem where name="%computername%" set AutomaticManagedPagefile=False
wmic pagefileset where name="C:\\pagefile.sys" delete
SetLocal EnableExtensions
 
REM Delete UserAssist count:
reg DELETE "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count" /f
reg DELETE "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{F4E57C4B-2036-45F0-A9AB-443BCFE33D9F}\Count" /f
 
REM Disable Prefetch and SysMain:
Reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v EnablePrefetcher /t REG_DWORD /d 0 /f
Reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v EnableSuperfetch /t REG_DWORD /d 0 /f
 
REM Enable USB Detection:
Reg ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-DriverFrameworks-UserMode/Operational" /v Enabled /t REG_DWORD /d 1 /f
schtasks.exe /Create /XML "C:\Tools\detect_usb.xml" /TN "Detect_USB"
wevtutil set-log Microsoft-Windows-TaskScheduler/Operational /e:true
wevtutil sl Microsoft-Windows-DriverFrameworks-UserMode/Operational /e:false
wevtutil sl Microsoft-Windows-DriverFrameworks-UserMode/Operational /e:true
 
REM Setup Hourly Tasks:
schtasks.exe /Create /XML "C:\Tools\run_hourly_tasks.xml" /TN "Run_Hourly_Tasks"
 
REM Enable Powershell to run unrestricted:
Reg ADD "HKLM\Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell" /v ExecutionPolicy /t REG_SZ /d Unrestricted /f
 
REM Install python:
cd c:\tools
curl https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe -o python_install.exe
python_install.exe InstallAllUsers=0 TargetDir="C:\Python" /quiet 
setx PATH "C:\python;%PATH%"
set PATH=C:\python;%PATH%
 
REM Install required python modules:
python -m pip install pywin32
python -m pip install win32_setctime
python -m pip install bs4
python -m pip install google
python -m pip install selenium
 
REM Install chromedriver:
curl https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_win32.zip -o chromedriver.zip
tar -xf chromedriver.zip

REM Setup EventLogEdit:
curl -L https://github.com/3gstudent/Eventlogedit-evtx--Evolution/releases/download/v1.1.0/Eventlogedit-evtx--Evolution-master-v1.1.zip -o Eventlogedit-evtx.zip
tar -xf Eventlogedit-evtx.zip
ren Eventlogedit-evtx--Evolution-master-v1.1 Eventlogedit-evtx
 
REM Download and install 7zip:
curl https://www.7-zip.org/a/7z2201-x64.exe -o 7zip.exe
7zip.exe /S
 
REM Shutdown:
shutdown /s /f /t 0
