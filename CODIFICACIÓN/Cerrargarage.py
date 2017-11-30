import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin_number = 11
GPIO.setup(pin_number, GPIO.OUT)
frequency_hertz = 50
pwm = GPIO.PWM(pin_number, frequency_hertz)
left_position = 0.40
right_position = 2.5
middle_position = (right_position - left_position) / 2 + left_position
positionList = [middle_position]
ms_per_cycle = 1000 / frequency_hertz

for i in range(3):
	for position in positionList:
		duty_cycle_percentage = position * 100 / ms_per_cycle
		print("Position: " + str(position))
		print("Duty Cycle: " + str(duty_cycle_percentage))
		print("")
		pwm.start(duty_cycle_percentage)
		time.sleep(.5)


pwm.stop()
GPIO.cleanup()
