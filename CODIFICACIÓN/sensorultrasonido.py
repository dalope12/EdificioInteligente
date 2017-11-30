
import time
import RPi.GPIO as GPIO
# Configurar el GPIO con convenio de numerado BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# trig (cable amarillo en el prototipo)
GPIO.setup(20, GPIO.OUT)
# echo (cable verde en el prototipo)
GPIO.setup(21, GPIO.IN)

pin_number = 17
GPIO.setup(pin_number, GPIO.OUT)
frequency_hertz = 50
pwm = GPIO.PWM(pin_number, frequency_hertz)
left_position = 0.40
right_position = 2.5
middle_position = (right_position - left_position) / 2 + left_position
positionList = [left_position]
ms_per_cycle = 1000 / frequency_hertz

def abrirpuerta():
    for i in range(3):
                for position in positionList:
                    duty_cycle_percentage = position * 100 / ms_per_cycle
                    print("Position: " + str(position))
                    print("Duty Cycle: " + str(duty_cycle_percentage))
                    print("")
                    pwm.start(duty_cycle_percentage)
                    time.sleep(.5)

    
try:
    while True:
        start = 0
        end = 0
        # Configura el sensor
        GPIO.output(20, False)
        time.sleep(2) # 2 segundos para hacer el programa usable
        # Empezamos a medir
        GPIO.output(20, True)
        time.sleep(10*10**-6) #10 microsegundos
        GPIO.output(20, False)

        # Flanco de 0 a 1 = inicio 
        while GPIO.input(21) == GPIO.LOW:
            start = time.time()
            
        # Flanco de 1 a 0 = fin
        while GPIO.input(21) == GPIO.HIGH:
            end = time.time()
        
        # el tiempo que devuelve time() estÃ¡ en segundos
        distancia = (end-start) * 343 / 2
        if distancia != 0.0:
            abrirpuerta()
            

        pwm.stop()
    
        print ("Distancia al objeto =", str(distancia))
        
except KeyboardInterrupt:
    print("\nFin del programa")
    GPIO.output(20, False)
    GPIO.cleanup()
