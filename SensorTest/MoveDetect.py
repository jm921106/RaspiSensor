import io
import RPi.GPIO as IoPort
import time
# import TcpWork
# import SndProt
# import picamera

NaPiOn = 20
Led = 17

IoPort.setwarnings(False)
IoPort.setmode(IoPort.BCM)
IoPort.setup(NaPiOn, IoPort.IN)
IoPort.setup(Led, IoPort.OUT)

# camera = picamera.PiCamera()
# Tcp = TcpWork.TcpWorl()
# Tcp.Connect('192.168.1.53', 20001)
# Prot = SndProt.SndProt()

while True :
    print(IoPort.input(NaPiOn))
    if IoPort.input(NaPiOn) == True:
        IoPort.output(Led, False)
    else :
        IoPort.output(Led, True)
    time.sleep(1)
