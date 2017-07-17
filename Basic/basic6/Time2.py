import RPi.GPIO as IoPort
import time
import array

class LED:
    def __init__(self):
        self.Led1 = 4
        self.Led2 = 17
        self.Led3 = 27
        self.Led4 = 22

        IoPort.setmode(IoPort.BCM)
        IoPort.setup(self.Led1, IoPort.OUT)
        IoPort.setup(self.Led2, IoPort.OUT)
        IoPort.setup(self.Led3, IoPort.OUT)
        IoPort.setup(self.Led4, IoPort.OUT)

    def Ledon(self, pos):
        if pos == 1:
            IoPort.output(self.Led1, True)
        elif pos == 2:
            IoPort.output(self.Led2, True)
        elif pos == 3:
            IoPort.output(self.Led3, True)
        elif pos == 4:
            IoPort.output(self.Led4, True)

    def Ledoff(self, pos):
        if pos == 1:
            IoPort.output(self.Led1, False)
        elif pos == 2:
            IoPort.output(self.Led2, False)
        elif pos == 3:
            IoPort.output(self.Led3, False)
        elif pos == 4:
            IoPort.output(self.Led4, False)

    def Toggle(self,pos,dly=None, dlyoff=None):
        if dly == None:
            self.Ledon(pos)
            time.sleep(0.2)
            self.Ledoff(pos)
            time.sleep(0.2)
        else :
            if dlyoff == None:
                self.Ledon(pos)
                time.sleep(dly)
                self.Ledoff(pos)
                time.sleep(dly)
            else :
                self.Ledon(pos)
                time.sleep(dly)
                self.Ledoff(pos)

def KeyInput (key) :
    if IoPort.input(key) == True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key) == True:
            break
    time.sleep(0.1)
    return True

ary1 = array.array('1')
Led = LED()

Key1 = 13
Key2 = 6

IoPort.setmode(IoPort.BCM)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)


print('program start !!!')

while True:
    if KeyInput(Key2) == True:
        break

print (' Start Time Check !')

tme = 0
while True:
    Led.Ledoff(1)
    while True:
        if IoPort.input(key2) == False:
            ary1.appent(tme)
            tme = None
            break
        time.sleep(0.0098)
        tme += 1
        if IoPort.input(Key1) == False:
            break
    if tme == None:
        break
    ary1.append(tme)
    Led.Ledon(1)
    while True:
        if IoPort.input(Key2) == False:
            ary1.append(tme)
            tme = None
            break
        time.sleep(0.0098)
        tme += 1
        if IoPort.input(Key1) == True:
            break
    if tme == None:
        break

    # working.... 