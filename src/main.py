# main.py -- put your code here!
import pycom
import time
import machine


adc = machine.ADC()           # create an ADC object
apin = adc.channel(pin='P17') # Listening to Pin 17

while (True):
    time.sleep(0.5)
    value = apin()
    print("Val = %d" %(value))