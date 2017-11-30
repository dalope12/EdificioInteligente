import RPi.GPIO as GPIO
import time

a = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(a,GPIO.OUT)

GPIO.output(a,GPIO.HIGH)
