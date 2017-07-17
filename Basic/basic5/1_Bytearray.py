bts1 = b'ABCD'
bte1 = bytearray(bts1)
bte2 = bytearray('EFGHI', 'utf-8')
bte3 = bytearray(range(0,5))
bte4 = bytearray()
bte4.append(4)
bte4.insert(0,3)
bte4 += bts1
bte5 = bte1 + bte2

print bte1
print bte2
print bte3
print bte4
print bte5
