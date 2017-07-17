import RPi.GPIO as IoPort
import time

import struct

def getbinary(dgt):
    bstr1 = bin(dgt)
    bstr2 = ''
    for i in range (2, len(bvl)):
        ch = bvl[7-i]
        if ch == '1':
            IoPort.output(Led, True)
        else:
            IoPort.output(Led, False)
        IoPort.output(Clk, True)
        time.sleep(0.2)
        IoPort.output(Clk, False)
        time.sleep(0.2)

Led = 4
Clk = 13

IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Clk, IoPort.OUT)

while True:
    rcv = raw_input("input number :")
    try :
        rnum = float(rcv)
    except:
        print ('bad number !, try again')
    rbte = struct.pack('<f', rnum)
    for bt in rbte:
        bvl = getbinary(bt)
        print(bvl)
        BitStream(bvl)

