import os 
from collections import OrderedDict
import string


now = 0
last = 0

'''
## guess length 
for i in range(30):
    cmd = "echo "+'X'*i+" | ../../../../../pin -t ../../obj-intel64/count.so -- ./crackme" 
    result =os.popen(cmd).read()
    result = result.split('\n')[-2]
    now = int(result)
    print("len={:2d}  ins_nums = {} delta = {}".format(i, now , now-last))
    last = now
'''


strs = string.ascii_letters + string.digits
flag = "........"

cmd = "echo "+flag+" | ../../../../../pin -t ../../obj-intel64/count.so -- ./crackme" 
result =os.popen(cmd).read()
result = result.split('\n')[-2]
last = int(result)

for i in range(8):
    for j in strs:
        flag =flag[:i]+ j+flag[i+1:] 
    

        cmd = "echo "+flag+" | ../../../../../pin -t ../../obj-intel64/count.so -- ./crackme" 
        result =os.popen(cmd).read()
        result = result.split('\n')[-2]
        now = int(result)
        if(now-last > 1000):
            
            print("flag = {}  ins_nums = {} delta = {}".format(flag, now , now-last))
            last = now 
            break 
        else :
            last= now

        

