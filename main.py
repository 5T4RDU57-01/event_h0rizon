from argparse import ArgumentParser, Namespace
from sys import argv
import os

from helpers import encrypt, decrypt, generate_key, encrypt_decrypt_folder

def main():

    message_code: int = do_everything()

    print_message(message_code)
    
    return 0


# Does everything
# Encrypts or decrypts a file or a folder, or generates an encryption key  
def do_everything() -> int:
    args = get_args()

    ##  ENCRYPTION  ##
    if args.encrypt:
        # Initialize the file/ folder and the key
        file = args.encrypt[0]
        key = args.encrypt[1]

        # See if the file/folder and key are valid
        if validation(file, key):
            # If the user gives a folder
            if os.path.isdir(file):
                encrypt_decrypt_folder(encrypt, file, key)
            
            # If the user only gives a file
            else:
                encrypt(file, key)
        
        # If the file/folder or key is invalid 
        else:
             return 1
    ##  ENCRYPTION  ##
    
    ##  DECRYPTION ##
    elif args.decrypt:
        # Initialize the file/ folder and the key

        file = args.decrypt[0]
        key = args.decrypt[1]
        
        # See if the file/folder and key are valid
        if validation(file, key):
            # If the user gives a folder
            if os.path.isdir(file):
                encrypt_decrypt_folder(decrypt, file, key)
            # If the user only gives a file
            else: 
                decrypt(file, key)
        
        # If the file/folder or key is invalid 
        else:
            return 1
        
    ##  DECRYPTION ##
    
    ##  KEY GENERATION  ##
        
    elif args.generate:
        key_name = args.generate[0]
        generate_key(key_name)

    ##  KEY GENERATION  ##
    
    return 0 
        
# Validates the file or folder and the symmetric key given by the user
def validation(file: str, key: str) -> bool:

    return (
        # If the file/folder is an actual path
        os.path.exists(file) and 
        # If the key is an actual path
        os.path.exists(key) and 
        # If the key has the right extention
        str(os.path.basename(key)).endswith(".key"))


# Gives the Namespace of all the args
def get_args() -> Namespace:
    parser = ArgumentParser()


    group = parser.add_mutually_exclusive_group(required=True)
    ##  <ENCRYPTION>  ##
    group.add_argument("-e","--encrypt", 
                            help="Encrypts a file or folder",
                            metavar=("filename", "keyname"),
                            nargs=2)
    ##  </ENCRYPTION>  ##

    ##  <DECRYPTION> ##
    group.add_argument("-d","--decrypt", 
                            help="Decrypts the file or folder",
                            metavar=("filename", "keyname"),
                            nargs=2)
    ##  </DECRYPTION> ##

    ##  <KEY GENERATION>  ##
    group.add_argument("-g","--generate", 
                            help="Generates a symmetric encryption key",
                            metavar=("keyname"),
                            nargs=1)
    ##  </KEY GENERATION>  ##

    args: Namespace = parser.parse_args()
   
    return args


# Given a code, prints a message
def print_message(code: int) -> None:
    
    messages: dict = {
        0 : "Action completed successfully!",
        1 : "Invalid File or keyname! (key must have '.key' extention)" ,
    }

    print(messages[code])


if __name__ == "__main__":
    main()
