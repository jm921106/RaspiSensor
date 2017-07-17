import RPi.GPIO as IoPort

Sw1 = 6
End = 13
Led = 4

IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Sw1, IoPort.IN)
IoPort.setup(End, IoPort.IN)

Count = 0

while Count == 0:
    rcv = IoPort.input(Sw1)
    if IoPort.input(End) == False:
        Count = 1
    IoPort.output(Led, rcv)
    
IoPort.output(Led, False)
