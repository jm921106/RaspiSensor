import serial
import time

class SrlLCD:

    def __init__(self, Baud):
        print("__init__")
        self.srl = serial.Serial('/dev/ttyAMA0', baudrate = Baud)

    def Print (self, str1) :
        print(str)
        self.SendCmd('$PRINT ' + str1 + '\n')

    def Clear (self):
        print("$CLEAR")
        self.SendCmd('CLEAR\n')

    def Home (self):
        print("$GO 1 1")
        self.Move(1,1)

    def Move(self, Row, Col):
        str1 = "$GO " + str(Row) + " " + str(Col) + "\n"
        print(str1)
        self.SendCmd(str1)

    def Cursor(self, View, Blink):
        str1 = "$CURSOR " + str(View) + " " + str(Blink) + "\n"
        print(str1)
        self.SendCmd(str1)

    def SendCmd(self, str1):
        bte = bytearray()
        for ch in str1:
            bte.append(ord(ch))
            self.srl.write(bte)
            time.sleep(0.05)


Lcd = SrlLCD(9600)

Lcd.Clear()
Lcd.Move(1,1)
Lcd.Print("This is Test Str")
Lcd.Move(2,1)
Lcd.Print("No : ")
Lcd.Move(2,6)
Lcd.Print("123456")
Lcd.Print("7890")
Lcd.Home()
Lcd.Cursor(1,1)