import RPi.GPIO as IoPort
import time

import TcpWork

# import sys
# sys.path.append('../basic7')
# sys.path.insert(0, '../basic7/TcpWork')


Led = 4
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
for i in range(0, 30):
    IoPort.output(Led, True)
    time.sleep(0.5)
    IoPort.output(Led, False)
    time.sleep(0.5)
IoPort.output(Led, False)

Tcp = TcpWork()

try:
    Tcp.Accept('192.168.10.6', 20004)
    Pre = time.clock()
    Sum = 0
    Tcp.Blocking(0)
    while True:
        Str1 = 'Sum = ' + str(Sum) + '\r\n'
        Tcp.SendStr(Str1)
        while True:
            RcvNo = Tcp.ReceiveStr()
            if RcvNo != None:
                if RcvNo.isdigit() == True:
                    Sum = Sum + int(RcvNo)
                NowClk = time.clock()
                if (NowClk - Pre) >= 1:
                    Pre = NowClk
                    break
except:
    IoPort.output(Led, False)