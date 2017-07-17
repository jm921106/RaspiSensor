import RPi.GPIO as IoPort
import time

import TcpWork


def KeyInput(key):
    if IoPort.input(key) == True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key) == True:
            break
    time.sleep(0.1)
    return True

KeyW = 13
IoPort.setmode(IoPort.BCM)
IoPort.setup(KeyW, IoPort.IN)
Tcp = TcpWork.TcpWork()
Tcp.Connect('192.168.10.6', 20004)
print ('connected ... ')

Tcp.Blocking(0)

while True:
    NbStr = Tcp.ReceiveStr()
    if NbStr != None:
        print (NbStr)
    if KeyInput(KeyW) == False:
        continue
    StrDta = input("Input Message : ")
    Tcp.SendStr(StrDta)