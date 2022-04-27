import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

#================================================

#GPIO PINS
dac    = [26, 19, 13,  6, 5, 11,  9, 10]
leds   = [21, 20, 16, 12, 7,  8, 25, 24]
comp   =  4
troyka = 17

#================================================
#akk GPIO in dac as output

GPIO.setup(dac,  GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)

#================================================

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

#------------------------------------------------

def dec2bin_volume(value):

    str = [int(element) for element in bin(value)[2:].zfill(8)]
    for i in range (8):

        if str[i] == 1:

            for ct in range(8-i):

                str[i + ct] = 1

    return str

#------------------------------------------------

def adc():                          # ADC function

    digit = 7
    return_value = 0

    for ct in range (8) :

        dac_inp = pow(2, digit)
        sgnl = dec2bin(dac_inp + return_value)

        GPIO.output(dac, sgnl)
        time.sleep(0.001)

        comp_out = GPIO.input(comp)

        if comp_out == 1:
            return_value += dac_inp

        digit -= 1

    return return_value

#------------------------------------------------

def show_volume(value):                 # converts 255 value to 'volume' value

    number = (int) (value * 8 / 255)
    # print('Number ')
    # print(number)

    str = [0, 0, 0, 0, 0, 0, 0, 0]
    for ct in range (number):

        str[7 - ct] = 1

    GPIO.output(leds, str)

#================================================

data = []                               # empty data list

try:

    #===============MEASURING====================

    start = time.time()                 # save start value of time

    GPIO.output(troyka, 1)              # 3.3 V on troyka input
    cur_volt = 0                        # current voltage

    while cur_volt < 3.0:

        adc_value = adc()               # value from 0 to 255
        cur_volt = 3.3 * (adc_value) / 256
                                        # voltage value

        data.append(cur_volt)           # sace cur_volt in list 'data'

        print ('ADC value : ')
        print (adc_value)
        print (' Input voltage in V: {:.2f} \n'.format(cur_volt))
                                        # print current voltage

        show_volume(adc_value)          # show 'volume' on leds

    charge = time.time() - start        # sace time of charging

    GPIO.output(troyka, 0)              # 0 V on troyka inpu

    while cur_volt > 0.06:

        adc_value = adc()               # value from 0 to 255
        cur_volt = 3.3 * (adc_value) / 256
                                        # voltage value

        data.append(cur_volt)           # sace cur_volt in list 'data'

        print ('ADC value : ')
        print (adc_value)
        print (' Input voltage in V: {:.2f} \n'.format(cur_volt))

        show_volume(adc_value)          # show 'volume' on leds

    total = time.time() - start

    discharge = total - charge

    #===============SHOWING_GRAPH================

    plt.plot(data)                      # build plot
    plt.savefig('7-1-graph.png')        # save to png

    plt.show()                          # show

    #===============SAVING=RESULTS===============

    data_string = [str(item) for item in data]
                                        # convert to string array

    #---------------SAVING_DATA------------------

    with open("7-1-data.txt", "w") as data_file:

        for item in data_string:

            data_file.write(item)
            data_file.write("\n")

    #---------------SAVING_SETTINGS--------------

    with open("7-1-settings.txt", "w") as settings_file:

        settings_file.write("General information: \n ")

        settings_file.write('Total     time: {} \n'.format(total)) 
        settings_file.write('Charge    time: {} \n'.format(charge))
        settings_file.write('Discharge time: {} \n'.format(discharge))

        settings_file.write('Discr: {} \n'.format(total / len(data)))
        settings_file.write('Quant: {} \n'.format(3.3/256))



#================================================

finally:

#turn on leds before end
    GPIO.output(troyka, 0)
    GPIO.output(dac , 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()