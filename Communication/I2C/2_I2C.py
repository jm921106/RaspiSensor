# import time, smbus
# import RPi.GPIO as IoPort
#
# class I2C :
#     def __init__(self):
#         self.bus = smbus.SMBus(1)
#
#     def Write(self, adr, pos, dta):
#         self.bus.write_byte_data(adr, pos, dta)
#         time.sleep(0.01)
#
#     def Read(self, adr, pos):
#         rcv = self.bus.read_byte_data(adr, pos)
#         time.sleep(0.01)
#         return rcv
#
# def KeyInput(key):
#     if IoPort.input(key) == True:
#         return False
#     time.sleep(0.1)
#     while True:
#         if IoPort.input(key) == True:
#             break
#     time.sleep(0.1)
#     return True
#
# def SaveString():
#     while True:
#         rev = input("Input String (pos, String) : ")