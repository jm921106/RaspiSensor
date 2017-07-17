lst = list()

while True:
    rcv = raw_input('Input (Name , Count , Cost) : ')
    trcv = rcv.split(',')
    if len(trcv) == 3 :
        lst.append(trcv)
    else :
        ldta = rcv.lower()
        if ldta == 'last':
            break
        else :
            print (rcv, ' is not acceptable data. Input data ! ')

print 'Name, Count , Cost'

for sm in lst :
    print(sm)