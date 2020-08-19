import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED=23
PUSH=18

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(PUSH, GPIO.IN)

try:
	while(True):
		if GPIO.input(PUSH)==GPIO.HIGH:
			GPIO.output(LED, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(LED, GPIO.LOW)
			time.sleep(1)

except KeyboardInterrupt:
	GPIO.output(LED,GPIO.LOW)
	GPIO.cleanup()