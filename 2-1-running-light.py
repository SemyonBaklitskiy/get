import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range(3):
    index = 7
    for j in leds:
        GPIO.output(leds[index], 1)
        time.sleep(0.2)
        GPIO.output(leds[index], 0)
        index -= 1

GPIO.output(leds, 0)
GPIO.cleanup