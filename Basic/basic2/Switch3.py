import RPi.GPIO as IoPort

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
Key1 = 6
Led1 = 4
Led2 = 17

IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)

State = 1

while State <= 4:
    DisplayState(State)
    while True:
        if IoPort.input(Key1) == False:
            break
    while True:
        if IoPort.input(Key1) == True:
            break
    State += 1

DisplayState(1)