# MultiBit Classic Wallet Recovery Toolkit

A guide and toolkit for recovering lost Bitcoin wallets created using **MultiBit Classic** (2011–2017). Includes recovery steps, legacy scripts, and tools for extracting private keys using `btcrecover` and Python 2.7.
> [!WARNING]
> This toolkit is intended only for recovering wallets that you personally own.
>
> Never upload wallet files, private keys, seed phrases, passwords, or recovery output to GitHub.
>
> Perform recovery operations offline whenever possible.
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

## MultiBit Classic Installer (Archived Locally)

The original MultiBit Classic installer has been recovered from an old Downloads folder.

**Details:**  
**File name:** `multibit-classic-0.5.18-setup.exe`  
**Version:** 0.5.18  
**Recovered from:** Personal archive (Downloads folder, circa 2013)  
**SHA-256 checksum:**

```diff
+ dc0c2ef689507c57347c0cbed58ea90fe12617a6fb026b308e81ec2127531b7e
```

**Tested:** ✅ Yes (offline use only)  
**Status:** Working GUI; supports wallet loading and private key export  

> ⚠️ This file is not included in the repository due to GitHub’s restrictions on binaries and licensing concerns.  
> Always verify file integrity using the SHA-256 hash and run only in a secure, offline environment.

**Trusted sources for download:**
- [archive.org — MultiBit Classic 0.5.18](https://archive.org/details/MultiBitClassic-0.5.18)
- [Pascal Bergeron — Where to Download MultiBit Classic](https://pascal-bergeron.com/en/posts/where-to-download-multibit-classic/)

**Before running any downloaded software:**
- Verify checksums whenever possible.
- Scan downloaded files with your preferred antivirus solution.
- Perform wallet recovery operations offline whenever practical.

## Quick Start

```bash
# Install protobuf
C:\Python27\python.exe -m pip install protobuf

# Run wallet-tool to check wallet contents
C:\Python27\python.exe tools\wallet-tool.py "path\to\wallet.wallet"

# Run btcrecover with password list
C:\Python27\python.exe btcrecover.py --wallet "path\to\wallet.wallet" --passwordlist my-passwords.txt
```

---

## Example Paths

```bash
# Example paths from a recovery setup (run in the commandline "cmd")
C:\Python27\python.exe
C:\Users\ExampleUser\Documents\btcrecover\btcrecover-master\
G:\MultiBit\multibit.wallet
```

---

## Sweep to Electrum

- Install [Electrum](https://electrum.org/)  
- Create new wallet > Import private key  
- Send to a secure modern wallet

---

## References

- [MultiBit Wiki](https://en.bitcoin.it/wiki/MultiBit)  
- [btcrecover GitHub](https://github.com/gurnec/btcrecover)  
- [Public key to BTC address](https://gobittest.appspot.com/Address)

---

## License

MIT

---

**Created by GenuinePR ** — after successfully recovering a MultiBit Classic wallet from 2013.
