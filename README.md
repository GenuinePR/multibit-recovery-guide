# MultiBit Classic Wallet Recovery Toolkit

A guide and toolkit for recovering lost Bitcoin wallets created using **MultiBit Classic** (2011–2017). Includes recovery steps, legacy scripts, and tools for extracting private keys using `btcrecover` and Python 2.7.

---

## Features

- Step-by-step recovery guide  
- Scripts to extract wallet contents  
- References for MultiBit and `btcrecover`

> ⚠️ For educational use only. Never upload private keys or `.wallet` files to GitHub.

---

## Requirements

- Python 2.7  
- [`btcrecover`](https://github.com/gurnec/btcrecover)  
- Java 8 (optional, for MultiBit GUI)  
- MultiBit `.wallet` file(s)

> Note: Recent versions of `btcrecover` no longer include `wallet-tool.py` or MultiBit-specific scripts. Recreated versions are included here.

---

## Quick Start

```bash
# Install protobuf
C:\Python27\python.exe -m pip install protobuf

# Run wallet-tool to check wallet contents
C:\Python27\python.exe tools\wallet-tool.py "path\to\wallet.wallet"

# Run btcrecover with password list
C:\Python27\python.exe btcrecover.py --wallet "path\to\wallet.wallet" --passwordlist my-passwords.txt
