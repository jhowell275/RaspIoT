import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)

True = 1

while True > 0:
  print "am inside the loop"
  time.sleep(3)


  # print "LED on"
  # GPIO.output(7,GPIO.HIGH)
  # time.sleep(6)
  # print "LED off"
  # GPIO.output(7,GPIO.LOW)
  # time.sleep(5)
