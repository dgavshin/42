#!/usr/bin/env python3

from sys import argv
from binascii import hexlify

command = argv[1][::-1]
pieces = [command[i:i+4] for i in range(0, len(command), 4)]
for piece in pieces:
    print(f"push 0x{hexlify(piece.encode()).decode()}")

