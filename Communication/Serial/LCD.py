import serial
import time

class SrlLCD :

    def __init__(self, Baud):
        print("__init__")
        self.srl = serial.Serial('/dev/ttyAMA0', baudrate = Baud)

    def SendCmd(self, str1):
        print("SendCmd : " + str1)
        try:
            bte = bytearray()
            for ch in str1:
                bte.append(ord(ch))
            self.srl.write(bte)
        except Exception as err:
            print(err)

Lcd = SrlLCD(9600)
str1 = "$CLEAR\n"
Lcd.SendCmd(str1)
str1 = "$PRINT Hello World ~ \n"
Lcd.SendCmd(str1)
str1 = "$GO 2 1 \n"
Lcd.SendCmd(str1)