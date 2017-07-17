import RPi.GPIO as IoPort
import time

def DisplayState (Ld1, Ld2) :
    IoPort.output(Led1, Ld1)
    IoPort.output(Led2, Ld2)

def StateWork (St) :
    if St == 1:
        return False, False
    if St == 2:
        return True, False
    if St == 3:
        return False, True
    if St == 4:
        return True, True

# Key1 = 6
# Key2 = 13
Led1 = 4
Led2 = 17

IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)
# IoPort.setup(Key1, IoPort.IN)
# IoPort.setup(Key2, IoPort.IN)

State = 1

while True:
    Ld1, Ld2 = StateWork(State)

    # print StateWork(State) = (True, False)

    DisplayState(Ld1, Ld2)
    State += 1
    time.sleep(0.4)
    if State > 4:
        State = 1
