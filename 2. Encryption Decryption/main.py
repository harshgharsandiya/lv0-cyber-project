from cryptography.fernet import Fernet
import sys

#Generate key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#Load key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

#Encrypt File
def encrypt_file(file_name, key):
    try:
        with open(file_name, "rb") as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(file_name, "wb") as file:
            file.write(encrypted_data)
        print(f"File {file_name} encrypted successfully")
    except FileNotFoundError:
        print(f"Error: File {file_name} not found!")
        
def decrypt_file(file_name, key):
    try:
        with open(file_name, "rb") as file:
            encrypted_data = file.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_name, "wb") as file:
            file.write(decrypted_data)
        print(f"File {file_name} decrypted successfully.")
    except FileNotFoundError:
        print(f"Error: File {file_name} not found!")
    except Exception as e:
        print(f"Error: Unable to decrypt file {e}")

def user_menu():
    print("[1]. For Encrypt File\n[2]. For Decrypt File\n[0]. Exit Program")

if __name__ == "__main__":
    generate_key()
    key = load_key()
    
    while(1):
        user_menu()
        
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                file_name = input("File to encrypt: ")
                encrypt_file(file_name, key)
            elif choice == 2:
                file_name = input("File to decrypt: ")
                decrypt_file(file_name, key)
            elif choice == 0:
                print("Program Terminated...")
                sys.exit(0)
            else:
                print("Enter valid choice 1,2 or 0")
        except ValueError:
            print("Error: Enter valid number")
                
        

    