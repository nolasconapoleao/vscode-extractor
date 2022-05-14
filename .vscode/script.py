import sys

filepath = ".vscode/settings.json"

import os
import re

# Calculate the subsystem
def retrieve_subsystem(argv):
    global new_value
    os.chdir(argv[1])
    
    while(1):
        if(os.path.exists('CMakeLists.txt')):
            new_value = os.getcwd()
            new_value = re.sub(r'.*\\services\\', '', new_value)
            new_value = re.sub('/','\\\\',new_value)
            
        if(os.path.exists('.vscode')):
            try:
                edit_settings()
            except:
                print("No service root found")
            return

        os.chdir('..')

import json

# Edit the settings
def edit_settings():
    with open(filepath, 'r') as file:
        json_data = json.load(file)
        json_data['service'] = new_value
        print(new_value)

    with open(filepath, 'w') as file:
        json.dump(json_data, file, indent=2)

if __name__ == "__main__":
   retrieve_subsystem(sys.argv)
   