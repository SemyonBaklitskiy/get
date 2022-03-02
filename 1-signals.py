import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

while True:
    if GPIO.input(4):
        GPIO.output(2, 0)
    else:
        GPIO.output(2, 1)