import RPi.GPIO as GPIO
import time

LED=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

PWM=GPIO.PWM(LED,100)
PWM.start(0)

delay =0.1
try:
	while True:
		for n in range(0,101):
			PWM.ChangeDutyCycle(n)
			time.sleep(delay)
		for n in range(100,-1,-1):
			PWM.ChangeDutyCycle(n)
			time.sleep(delay)
except KeyboardInterrupt:
	PWM.stop()
	GPIO.cleanup()