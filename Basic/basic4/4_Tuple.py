import RPi.GPIO as IoPort
import time

def KeyInput():
    while True:
        if IoPort.input(Key1) == False:
            break
    time.sleep(0.1)
    while True:
        if IoPort.input(Key1) == True:
            break
    time.sleep(0.1)

tpl = (1.2, 0.8, 1.2, 2.4)
Key1 = 6
Led1 = 4

IoPort.output(Led1, True)
time.sleep(1)
IoPort.output(Led1, False)

while True:
    KeyInput()
    print ('Signal Out Now')
    Sig = False;
    for i in range(0, len(tpl)):
        IoPort.output(Led1, Sig)
        time.sleep(tpl[i])
        Sig = not Sig
    IoPort.output(Led1, Sig)

