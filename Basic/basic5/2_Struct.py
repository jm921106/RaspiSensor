import struct
strc = struct.Struct('Bhl')
fmt = strc,format
print fmt

bte1 = strc.pack(1,2,3)
bte2 = struct.pack('Bhf', 1, 2, 2.5)
bte1 += bte1
bte3 = struct.pack('cs', b'a' , b'bcdef')
bte1 += bte3

print bte1

bte4 = struct.pack('<Bhf', 3, 4, 5.1)
print bte4

bte5 = struct.pack('<Bhlf', 3, 4, 5, 2.3)
print bte5

print bte2

bte6 = struct.unpack('Bhf', bte2)
print bte6

bte7 = struct.pack('hhf', bte6[0], bte6[1], bte6[2])
print bte7