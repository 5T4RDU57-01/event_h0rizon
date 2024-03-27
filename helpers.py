from cryptography.fernet import Fernet
import os

# Encrypts a file
def encrypt(filename: str , key: str) -> int:

    # Open and read the file with the key
    with open(key , 'rb') as fkey:
        key = fkey.read()
    
    fer = Fernet(key)
    
    # Read the plaintext
    with open(filename , 'rb') as file:
        plaintext = file.read()
    
    # Get the ciphertext
    ciphertext = fer.encrypt(plaintext)
    
    # Write the ciphertext to the file
    with open(filename , 'wb') as write_file:
        write_file.write(ciphertext)

    return 0 


# Decrypts a file
def decrypt(filename: str , key: str) -> int:

    # Open and read the file with the key
    with open(key , 'rb') as fkey:
        key = fkey.read()
    
    fer = Fernet(key)
    
    # Read the ciphertext
    with open(filename , 'rb') as file:
        ciphertext = file.read()
    
    # Get the plaintext
    plaintext = fer.decrypt(ciphertext)
    
    # Write the plaintext to the file
    with open(filename , 'wb') as write_file:
        write_file.write(plaintext)
    
    return 0 


# Generates a symmetric encryption key
def generate_key(name: str) -> int:
    
    name = f'{name}.key'

    # Generate a key
    key = Fernet.generate_key()

    # Make a file with the specified name and write the key to it
    with open(name , 'wb') as file:
        file.write(key)
    
    return 0 


# Encrypts or decrypts all the files in a directory
def encrypt_decrypt_folder(method : function, folder : str, key : str) -> None:
        
        # Initialize the function to be used (encrypt or decrypt)
        procedure = method

        # Get a list of all filepaths to be encrypted or decrypted
        filelist = []
        for root, dirs, files in os.walk(folder):
            #append the file name (whole path) to the list
            for file in files:
                
                # Make sure system or ini files don't get added
                base_name = os.path.basename(file).lower()

                if not base_name.startswith(".") and base_name != "desktop.ini":
                    filelist.append(os.path.join(root, file))
        
        # Encrypt or decrypt all the files
        for file in filelist:
            procedure(file, key)
