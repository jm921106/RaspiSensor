import time
import smbus

i2c = smbus.SMBus(1)
rcv = input("Input String : ")

pos = 0

for ch in rcv:
    i2c.write_byte_data(0x50, pos, ord(ch))
    time.sleep(0.01)
    pos = pos + 1

i2c.write_byte_data(0x50, pos, 0x0)
time.sleep(0.01)

str1 = ''
i=0

while True:
    brcv = i2c.read_byte_data(0x50, i)
    if(brcv == 0):
        break
    if i>255:
        break
    str1 = str1 + chr(brcv)
    i = i+1
    time.sleep(0.01)

print(str1)