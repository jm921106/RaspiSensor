import picamera
import time
camera = picamera.PiCamera()
camera.rotation = 90 # approve 0 90 180 270
camera.resolution = (1280, 720)
camera.start_preview()
camera.capture("cam_1.jpg")
time.sleep(2)
camera.capture("cam_2.jpg")
time.sleep(2)
camera.capture("cam_3.jpg")
camera.stop_preview()
camera.close()