with open("flag.enc","rb") as f:
    
    idd = 0 
    while( True):
        strs = f.read(4)
        
        if(not strs):
            break
        #print(idd)
        #print(strs)
        strs = int.from_bytes(strs, byteorder= 'little')
        
        idoe = idd+1
        dec = (strs -0x15be)/int((((idoe - (idoe >>  0x1f) & 1) + (idoe>> 0x1f) +1)))

        idd = idoe
        print(chr(int(dec)),end="")




