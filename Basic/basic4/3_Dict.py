dict1 = { 'A1' : 1, 'A2' : 'Test', 'A3' : 'Hello World', 'A4' : [1,2,3] }

dict2 = dict(A1 = 1, A2 = 'Test', A3 = 'Hello World', A4 = [1,2,3])

dict3 = dict([('kim',23), ('Lee', 'a45'), ('choi', [1,2,3])])

dict4 = dict()

if dict1 == dict2 :
    print (dict1)
    print (dict2)

for st in dict2 :
    print (st)
    print dict2[st]

print dict3


# dict[key] = value
dict3['kim'] = 'abc'

print dict3

# update
ref1 = { 'Lee' : 17 }
dict3.update(ref1)

print dict3

# insert
ref1 = { 'park' : 37 }
dict3.update(ref1)

print dict3


del dict3['choi']

print dict3

dict4 = dict3

# length
len1 = len(dict4)
print len1 , '; ', dict4

# reference dict4 > dict3
dict4.clear()
print(dict3, '; ', dict4)