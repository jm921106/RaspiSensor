from LCD2 import SrlLCD
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