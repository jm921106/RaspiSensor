def prg1():
    print 'Prog 1'

def prg2():
    print 'Prog 2'

def prg3():
    print 'Prog 3'

def prg4():
    print 'Prog 4'

tpl1 = (1,2,3,4)

print'tuple = ' , tpl1

print 'pos of 2 is ', tpl1.index(2)

print 'tpl2[2] is ', tpl1[2]

# tuple in tuple
tpl2 = (11, 'Test a', 88, tpl1)

for tp in tpl2:
    print(tp)

# function index okay
tpl3 = (prg1, prg2, prg3, prg4)
for tp in tpl3:
    tp()