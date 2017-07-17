lst1 = [3,2,1]
lst2 = [[1,5,3], [2,3,1], lst1]
lst3 = [x for x in range (0,10)]
lst4 = list(range(4,10))
lst5 = list()
lst5.append(lst2)

print lst1
print lst2
print lst3
print lst4
print lst5
print '\n'

lst3 = lst1 + lst2

print lst1
print lst2
print lst3
print lst4
print lst5
print '\n'

lst1.sort()
a = lst4.pop()
lst4.insert(3, 77)

print lst1
print lst2
print lst3
print lst4
print lst5
print '\n'

lstT = [lst1, lst2]
print lstT

