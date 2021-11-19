import os 
from collections import OrderedDict
import string


now = 0
last = 0

## guess length 
for i in range(30):
    cmd = "echo "+'X'*i+" | ../../../../../pin -t ../../obj-ia32/count.so -- ./Easy_ELF" 
    result =os.popen(cmd).read()
    result = result.split('\n')[-2]
    print(result)
    now = int(result)
    print("len={:2d}  ins_nums = {} delta = {}".format(i, now , now-last))
    last = now
