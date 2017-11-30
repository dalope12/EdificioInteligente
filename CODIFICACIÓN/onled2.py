import RPi.GPIO as GPIO
import time

d= 13
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(d,GPIO.OUT)

GPIO.output(d,GPIO.HIGH)
