import os, shutil

# Checking to see if base directories exist

if os.path.isdir('/Boilest/DB') == False:
    print ('/Boilest/DB directory does not exist, creating')
    os.mkdir('/Boilest/DB')
else:
    print ('/Boilest/DB exists, no action needed')

if os.path.isdir('/Boilest/Configurations') == False:
    print ('/Boilest/Configurations directory does not exist, creating')
    os.mkdir('/Boilest/Configurations')
else:
    print ('/Boilest/Configurations exists, no action needed')

if os.path.isdir('/Boilest/Logs') == False:
    print ('/Boilest/Logs directory does not exist, creating')
    os.mkdir('/Boilest/Logs')
else:
    print ('/Boilest/Logs exists, no action needed')

# Checking for atleast the base configuration

print ('Checking to see if /Boilest/Configurations is empty')

# Getting the list of directories 
dir = os.listdir('/Boilest/Configurations') 
  
# Checking if the list is empty or not 
if len(dir) == 0: 
    print("No Configurations, adding Defualt")
    shutil.copyfile('/Scripts/Templates/AV1_CRF20Preset4.json', '/Boilest/Configurations/AV1_CRF20Preset4.json') 
else: 
    print("Configurations detected, no action to take") 