#!/usr/bin/env python3
from binascii import unhexlify


# %p;%p; ... many times ... %p;
p = input("> ").strip().split(";")
print("".join([unhexlify(x[2:])[::-1].decode() for x in p]))