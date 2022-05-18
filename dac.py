import RPi.GPIO as GPIO 

dac = [ 26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while(1):
        a = input("Input int num from 0 to 255: ")
        if a == 'q':
            break
        try:
            if float(a) % 1 != 0:
                print("Not int")
                continue
            elif int(a) > 255:
                print("More than 255")
                continue
            elif int(a) < 0:
                print("less than 0")
                continue
            a = int(a)
            GPIO.output(dac, decimal2binary(a))
            print("Voltage:")
            print(3.3*a/255)
        except ValueError:
            print("NAN")