#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wallet-tool.py - Print addresses and private keys from a BitcoinJ-based .wallet file (e.g., MultiBit Classic)
# Originally by gurnec - https://github.com/gurnec/btcrecover

import sys
import os
import argparse
import base64

from google.protobuf import message
from google.protobuf.internal import decoder
from google.protobuf.internal import encoder

try:
    import wallet_pb2
except ImportError:
    print("Missing required protobuf definition. You must have 'wallet_pb2.py'.")
    sys.exit(1)

def read_wallet_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    wallet = wallet_pb2.Wallet()
    wallet.ParseFromString(data)
    return wallet

def dump_wallet(wallet):
    print("Wallet description: %s" % wallet.description)
    print("Encrypted: %s" % wallet.encryption_type)
    for key in wallet.key:
        pubkey = base64.b16encode(key.public_key).decode()

        # Safely handle presence of private key
        if hasattr(key, 'private_key') and key.HasField('private_key'):
            privkey = base64.b16encode(key.private_key).decode()
            priv_status = privkey
        else:
            priv_status = '[NO PRIVATE KEY]'

        print("Address label: %s" % key.label)
        print("Public key: %s" % pubkey)
        print("Private key: %s\n" % priv_status)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('wallet_file', help='Path to a MultiBit Classic .wallet file')
    args = parser.parse_args()

    wallet = read_wallet_file(args.wallet_file)
    dump_wallet(wallet)
