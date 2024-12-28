
# Basic File Encryption and Decryption

## Introduction  
This program allows you to **encrypt and decrypt any file** (not limited to text files) using the **AES encryption** algorithm from the `cryptography` library. This ensures secure encryption and easy decryption of files when needed.

---

## Features  
- Encrypt any file and save the encrypted version.  
- Decrypt the encrypted file back to its original content.  
- A simple user interface that allows you to choose between encryption and decryption.  

---

## Prerequisites  
- Python 3.x installed on your system.  
- `cryptography` library installed. To install it, run the following command:  
  ```
  pip install cryptography
  ```

---
## Usage
1. Clone or download the project files.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. Enter Your Choice
    - [1] for Encryption
    - [2] for Decryption
    - [0] for Exit Program
---

## Example

1. When encrypting:
   ```
   Enter your choice: 1
   Enter the file name to encrypt: test.txt
   File 'test.txt' encrypted successfully.
   ```

2. When decrypting:
   ```
   Enter your choice: 2
   Enter the file name to decrypt: test.txt
   File 'test.txt' decrypted successfully.
   ```

---

## Important Notes  
> Make sure to **keep your `key.key` file safe** as it is required for both encryption and decryption.
