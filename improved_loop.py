import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

True = 1

while (1):
  print "am inside the outer loop"
  if GPIO.input(21)==1:
    print "Alarm is armed - LED on"
    GPIO.output(7,GPIO.HIGH)
    time.sleep(4)
  else:
    print "Alarm is disarmed - LED off"
    GPIO.output(7,GPIO.LOW)
    time.sleep(4)
