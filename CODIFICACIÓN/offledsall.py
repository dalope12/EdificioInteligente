import RPi.GPIO as GPIO
import time

a = 26
d = 13
e = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(a,GPIO.OUT)
GPIO.setup(d,GPIO.OUT)
GPIO.setup(e,GPIO.OUT)

GPIO.output(e,GPIO.LOW)
GPIO.output(d,GPIO.LOW)
GPIO.output(a,GPIO.LOW)
