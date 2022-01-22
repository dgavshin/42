from sys import argv

UINT_MAX = 4294967295
BUFFER_ADDR = 0

with open(argv[1], "rb") as f:
    shellcode = f.read()
