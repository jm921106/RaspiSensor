import RPi.GPIO as IoPort
import time

def KeyInput (key) :
    if IoPort.input(key) == True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key) == True:
            break
    time.sleep(0.1)
    return True

def ViewLed (tur) :
    IoPort.output(Led1, tur[0])
    IoPort.output(Led1, tur[1])
    IoPort.output(Led1, tur[2])

def Init():
    global Led1, Led2, Led3, Key1, Key2, Key3, dct, snme
    Led1 = 4
    Led2 = 17
    Led3 = 27
    Key1 = 6
    Key2 = 13

    IoPort.setmode(IoPort.BCM)
    IoPort.setup(Led1, IoPort.OUT)
    IoPort.setup(Led2, IoPort.OUT)
    IoPort.setup(Led3, IoPort.OUT)
    IoPort.setup(Key1, IoPort.IN)
    IoPort.setup(Key2, IoPort.IN)

    S1 = [[False, False, True], 'S2', 'S3']
    S2 = [[False, True, False], 'S2', 'S3']
    S3 = [[False, True, True], 'S4', 'S5']
    S4 = [[True, False, False], 'S6', 'S4']
    S5 = [[True, False, True], 'S1', None]
    S6 = [[True, True, False], 'S5', 'S7']
    S7 = [[True, True, True], 'S5', 'S6']
    dct = { "S1" : S1, "S2":S2, "S3":S3, "S4":S4, "S5":S5, "S6":S6, "S7":S7 }
    snme = "S1"
    ViewLed(dct[snme][0])

Init()

while True:
    ViewLed(dct[snme][0])
    if KeyInput(key1) == True:
        snme = dct[snme][1]
        if snme == None:
            break
    if KeyInput(Key2) == True:
        snme = dct[snme][2]
        if snme == None:
            break
