import os 
from collections import OrderedDict
import string


now = 0
last = 0

strs = string.ascii_letters + string.digits
flag = "....."

cmd = "echo "+flag+" | ../../../../../pin -t ../../obj-ia32/count.so -- ./Easy_ELF" 
result =os.popen(cmd).read()
result = result.split('\n')[-2]
last = int(result)

for i in [1,4,2,0,3]:
    for j in strs:
        flag =flag[:i]+ j+flag[i+1:] 
    

        cmd = "echo "+flag+" | ../../../../../pin -t ../../obj-ia32/count.so -- ./Easy_ELF" 
        result =os.popen(cmd).read()
        result = result.split('\n')[-2]
        now = int(result)
        
        #print("flag = {}  ins_nums = {} delta = {}".format(flag, now , now-last))
        if(now-last > 0):
                
            print("flag = {}  ins_nums = {} delta = {}".format(flag, now , now-last))
            last = now 
            break 
        else :
            last= now

        

