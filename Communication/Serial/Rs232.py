import serial
import time

class Rs232:
    def __init__ (self, Baud):
        self.srl = serial.Serial('/dev/ttyAMA0', baudrate=Baud)

    def Send(self, dta):
        self.srl.write(dta)

    def Receive(self):
        sno = self.srl.inWaiting()
        if sno == 0:
            return None
        while True:
            time.sleep(0.01)
            sno2 = self.srl.inWaiting()
            if sno == sno2:
                btrcv = self.srl.read(sno)
                return btrcv
            sno = sno2