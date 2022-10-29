# ensbear_hinderdf

## User Guide

1. Download the source code by clicking **Code** follow by **Download ZIP** as shown below:

![image](https://user-images.githubusercontent.com/71330661/198842903-869599c2-c300-4d70-b0e7-c1310ea07a97.png)

2. Create Tools directory in C:\
3. Unzip ensbear_hinderdf-main.zip in C:\Tools
4. 

### Overall Process

#### Incident Tasks
1. Investigator plug in USB
2. [initial_setup.bat] Scheduler detect usb plug in event
3. [initial_setup.bat] Scheduler invoke Python script
4. [run.py] Pause event logging
5. [run.py] Script initiate lock screen
6. [run.py] Script reset account to random password
7. [delete_chrome_cache.py] Script to delete chrome cache
8. [run.py] Script to delete event logs related to powershell execution
9. [run.py] Script to delete the event for cleared event log (Event ID 104)
10. [run.py] Resume event logging

#### Daily Tasks via scheduler
1. [gen_files.py] Script to create decoy directories and files
2. [zipbomb.py] Script to create zip bombs
3. [gen_history.py, searches.txt] Script to generate random chrome searches


