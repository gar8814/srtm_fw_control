# SRTM Firware Control
## What you need 
- Install UHal: https://ipbus.web.cern.ch/doc/user/html/software/installation.html
- clone Firmware Control repo 
    - `git clone git@github.com:gar8814/srtm_fw_control.git <dir>`

# Adding new functionality
## Adding new subsystem and its options
In Menu.py add the menuTree dictionary
```py
"New System": {
    "options" : ['option num1', 'option num2', 'option num3'],
    "parent" : 'Main Menu'
}
```

this will translate to the user as: 

```bash
New System:
    1. option num1
    2. option num2
    3. option num3
    0. Back 
```

## Adding add to SRTM.py and FirmwareControl.py
### To implement new tests reutines
In SRTM.py new test routines can be implemented by defineing new methods in the SRTM class. These methods methods can 
then be called by FirmwareControl.py for each srtm by adding elif statement in the main while loop of FirmwareControl.run()
```py
elif command=="option":
    for i in range(len(self._srtms)):
        self._srtms[i].newSRTMFunction()
```
