import time
import picamera

camera = picamera.PiCamera()

camera.start_preview()
camera.preview.fullscreen = False
camera.preview.window = (0,0,640,480)
camera.start_recording('video.h264')

time.sleep(5)

camera.stop_recording()
camera.stop_preview()
camera.close()