# lockbox
Encrypt and decrypt files using **AES-256 (CBC mode)** with **PBKDF2 key derivation**.   Built for security and simplicity.

# Warning 
Use this repository for the understanding of ransomware attacks and learning purpose only, files cannot be recovered if password is lost. 
Always test with sample data first.

## ✨ Features

- 🔒 **AES-256 encryption** for all file types  
- 🔑 **PBKDF2 (100k iterations)** for strong password-based key derivation  
- 📂 Works recursively on entire folders  
- 🗑️ Optionally removes originals after encryption / `.enc` files after decryption  
- 🖥️ Tested on Linux (Kali), should work on any OS with Python 3.7+

## 📦 Requirements

- Python 3.7+  
- [PyCryptodome](https://pycryptodome.readthedocs.io/) library  

Install inside a virtual environment (recommended):


# Step by Step process
 1.Clone the repository
 
    git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPO>.git
 
    cd <YOUR-REPO>
 2.Activate the virtual environment

    source ~/cryptoenv/bin/activate
3.Encrypt the files:

  Make sure you are in the virtual environment
   
    python encryption.py

  Output: each .enc file becomes <filename>.enc , and the original file is removed

4.Decrypt the files:

   Make sure you are in the virtual environment and the your python and pip have the same path.

      python decryption.py
  Output: each .enc file is restored to its original , and the .enc is removed

  ## License
  This project is licensed undet the MIT License
  see LICENSE 

## Warning : 
Use this repository for the understanding of ransomware attacks and learning purpose only, files cannot be recovered if password is lost. 
Always test with sample data first.
