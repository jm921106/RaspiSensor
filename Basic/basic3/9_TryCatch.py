while True:
    rcv = raw_input ('input no. : ')

    try :
        ival = int (rcv)
        break
    except :
        print rcv, 'is not integer no. try again !'
        continue

print 'Reveived No. is ', ival