import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]
GPIO.setmode(GPIO.BCM)
for i in range(8): GPIO.setup(aux[i], GPIO.IN)
for i in range(8): GPIO.setup(leds[i], GPIO.OUT)

GPIO.output(leds, 0)