import RPi.GPIO as IoPort
import time

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

    def Ledon (self, pos):
        if pos == 1:
            IoPort.output(self.Led1, True)
        elif pos == 2:
            IoPort.output(self.Led2, True)
        elif pos == 3:
            IoPort.output(self.Led3, True)
        elif pos == 4:
            IoPort.output(self.Led4, True)

    def Ledoff (self, pos):
        if pos == 1:
            IoPort.output(self.Led1, False)
        elif pos == 2:
            IoPort.output(self.Led2, False)
        elif pos == 3:
            IoPort.output(self.Led3, False)
        elif pos == 4:
            IoPort.output(self.Led4, False)

    def Toggle(self, pos, dly):
            self.Ledon(pos)
            time.sleep(dly)
            self.Ledoff(pos)
            time.sleep(dly)

Led = LED()
while True:
    Led.Toggle(1, 0.4)
    Led.Toggle(2, 0.4)
    Led.Toggle(3, 0.4)
    Led.Toggle(4, 0.4)