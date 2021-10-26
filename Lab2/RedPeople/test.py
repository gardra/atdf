
idoe =2
index_add_1 = idoe
strs = ord("g")
print( int((strs*((idoe        - (idoe        >>  0x1f) & 1) + (idoe        >> 0x1f) +1)+0x15be)).to_bytes(4, "little"))

#(enc -0x15be)/int((((idoe - (idoe >>  0x1f) & 1) + (idoe>> 0x1f) +1)))

#print( int((strs*((index_add_1 - (index_add_1 >> 0x1f) & 1) + (index_add_1 >> 0x1f) + 1)+0x15be)).to_bytes(4,"little")) 
