import RPi.GPIO as IoPort
import time

def LedOn(Port, Delay):
    IoPort.output(Port, True)
    time.sleep(Delay)

def LedOn(Port, Delay):
    IoPort.output(Port, False)
    time.sleep(Delay)

def Send_S(Port):
    LedOn(Led,0.4)
    LedOff(Led,0.4)
    LedOn(Led,0.4)
    LedOff(Led,0.4)
    LedOn(Led,0.4)
    LedOff(Led,0.4)

Led = 18

IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
for I in range(0, 10):
    LedOff(Led, 2.4)
    Send_S(Led)
    # Send_O(Led)
    # Send_S(Led)