#!/usr/bin/env python3

xor_byte = [ord(a) ^ ord(b) for a,b in zip("Q}|u`sfg~sf{}|a3", "Congratulations")]
print(xor_byte)

print("Password is: ", 0x1337D00D - xor_byte[0])
# 322424827
