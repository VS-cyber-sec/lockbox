import os
import sys
import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

KEY_LENGTH = 32
SALT_SIZE = 16
IV_SIZE = 16
ITERATIONS = 100_000
CHUNK_SIZE = 64 * 1024

EXCLUDE_DIRS = ["/bin", "/boot", "/dev", "/etc", "/lib", "/proc", "/run", "/sbin", "/sys", "/usr", "/var"]

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def decrypt_file(filepath, password):
    try:
        with open(filepath, "rb") as f_in:
            salt = f_in.read(SALT_SIZE)
            iv = f_in.read(IV_SIZE)
            key = PBKDF2(password, salt, dkLen=KEY_LENGTH, count=ITERATIONS)
            cipher = AES.new(key, AES.MODE_CBC, iv)

            out_file = filepath[:-4]  # remove ".enc"

            with open(out_file, "wb") as f_out:
                while chunk := f_in.read(CHUNK_SIZE):
                    decrypted = cipher.decrypt(chunk)
                    if len(chunk) < CHUNK_SIZE:
                        decrypted = unpad(decrypted)
                    f_out.write(decrypted)

        os.remove(filepath)
        print(f"[+] Decrypted & deleted encrypted file: {filepath} -> {out_file}")

    except Exception as e:
        print(f"[!] Skipped {filepath} (error: {e})")

def decrypt_machine(password):
    for root, dirs, files in os.walk("/"):
        if any(root.startswith(ex) for ex in EXCLUDE_DIRS):
            continue

        for filename in files:
            if filename.endswith(".enc"):
                filepath = os.path.join(root, filename)
                decrypt_file(filepath, password)

if __name__ == "__main__":
    password = getpass.getpass("Enter password: ")
    print("[*] Starting full machine decryption (excluding system dirs)...")
    decrypt_machine(password)
