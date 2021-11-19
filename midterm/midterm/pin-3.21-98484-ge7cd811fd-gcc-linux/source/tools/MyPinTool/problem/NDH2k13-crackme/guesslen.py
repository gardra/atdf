import os 
from collections import OrderedDict
import string


now = 0
last = 0


## guess length 
for i in range(30):
    cmd = "echo "+'X'*i+" | ../../../../../pin -t ../../obj-intel64/count.so -- ./crackme" 
    result =os.popen(cmd).read()
    result = result.split('\n')[-2]
    now = int(result)
    print("len={:2d}  ins_nums = {} delta = {}".format(i, now , now-last))
    last = now
