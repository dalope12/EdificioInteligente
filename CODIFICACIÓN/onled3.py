import RPi.GPIO as GPIO
import time

e= 19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(e,GPIO.OUT)

GPIO.output(e,GPIO.HIGH)
