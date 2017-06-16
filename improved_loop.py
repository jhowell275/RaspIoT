import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)

armed = 1

while armed > 0:
  print "LED on"
  GPIO.output(7,GPIO.HIGH)
  time.sleep(6)
  print "LED off"
  GPIO.output(7,GPIO.LOW)
  time.sleep(5)
