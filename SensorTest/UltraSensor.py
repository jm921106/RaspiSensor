import RPi.GPIO as gpio
import time

trig = 20
echo = 21
print ("start")

gpio.setmode(gpio.BCM)
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

try :
    while True :
        gpio.output (trig, False)
        time.sleep(0.5)
        gpio.output (trig, True)
        time.sleep(0.00001)
        gpio.output(trig, False)

        while gpio.input(echo) == 0:
            pulse_start = time.clock()
        while gpio.input(echo) == 1:
            pulse_end = time.clock()

        pulse_duration = pulse_end - pulse_start
        print ("pulse_duration : " , pulse_duration)


        distance = pulse_duration * 17241
        distance = round(distance, 2)
        print ("Distance : " , distance, "cm")

except:
    gpio.cleanup()