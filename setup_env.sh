#!/bin/bash
# Script to set up Python virtual environment for AES encryption/decryption

# Folder where the venv will live
VENV_DIR="$HOME/cryptoenv"

# Create venv if it doesn’t exist
if [ ! -d "$VENV_DIR" ]; then
    echo "[+] Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate venv
source "$VENV_DIR/bin/activate"

# Install dependencies
echo "[+] Installing required packages..."
pip install --upgrade pip
pip install pycryptodome

echo "[+] Setup complete. To activate later, run:"
echo "    source $VENV_DIR/bin/a