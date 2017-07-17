import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)
IoPort.setup(18, IoPort.OUT)

IoPort.output(18, True)
time.sleep(2)
IoPort.output(18, False)