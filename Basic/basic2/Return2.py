import RPi.GPIO as IoPort
import time

# chattering exist !

def DisplayState (St) :
    if St == 1:
        IoPort.output(Led1, False)
        IoPort.output(Led2, False)
    elif St == 2:
        IoPort.output(Led1, True)
        IoPort.output(Led2, False)
    elif St == 3:
        IoPort.output(Led1, False)
        IoPort.output(Led2, True)
    elif St == 4:
        IoPort.output(Led1, True)
        IoPort.output(Led2, True)

def GetKey (key, St) :
    if IoPort.input(key) == True:
        return St
    time.sleep(0.1)

    while True:
        if IoPort.input(key) == True:
            break
    time.sleep(0.1)
    return St+1

Key1 = 6
Key2 = 13
Led1 = 4
Led2 = 17

IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)

State = 1

while True:
    DisplayState(State)

    if State == 1:
        State = GetKey(Key1, State)

    elif State == 2:
        State = GetKey(Key1, State)

        # end
        if GetKey(Key2, 0) > 0 :
            break

    elif State == 3:
        State = GetKey(Key1, State)

    else :
        State = GetKey(Key1, State)

        # end
        if GetKey(Key2, 0) > 0:
            break

    if State > 4 :
        State = 1

DisplayState(State)