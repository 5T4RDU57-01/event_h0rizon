#### Event Horizon
This is a command-line tool written in Python that allows users to encrypt or decrypt files and folders using a symmetric encryption key, or generate a new key.

## Usage
# Prerequisites
 Python 3.x
 cryptography library (pip install cryptography)

# Command Line Arguments
 -e, --encrypt <filename> <keyname>: Encrypts a file or folder using the specified key.
 -d, --decrypt <filename> <keyname>: Decrypts a file or folder using the specified key.
 -g, --generate <keyname>: Generates a new symmetric encryption key.

## Example Usage
# Encrypt a file:

 python main.py -e my_file.txt my_key.key

# Decrypt a folder:

python main.py -d my_folder my_key.key

# Generate a new key:

 python main.py -g new_key

## Files

 main.py: Contains the main program logic and command-line argument parsing.
 helpers.py: Contains helper functions for encryption, decryption, key generation, and folder encryption/decryption.

## How It Works
 The main.py file handles command-line arguments using the argparse library.
 The program can encrypt/decrypt a file or folder using a specified key, or generate a new key.
 Encryption and decryption are done using the cryptography.fernet module for symmetric encryption.

## Usage Notes
 Make sure to provide valid file paths and key names with the appropriate extensions (e.g., .key for keys).
 The program supports encrypting and decrypting folders recursively.

## Running the Program
 Install Python 3.x and the cryptography library.
 Open a terminal or command prompt.
 Navigate to the directory containing main.py and helpers.py.
 Use the command-line arguments as described above to encrypt, decrypt, or generate keys.
