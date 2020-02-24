import pycom
import time
import machine
import networkSetup
import struct
import ustruct   
import packageConverter

messenger = networkSetup.linkup() # Sending Object
i = 0

adc = machine.ADC()           # create an ADC object
apin = adc.channel(pin='P17') # Listening to Pin 17

while True:
    value = apin()
    if(messenger != None) :
        value = apin()
        testpack = packageConverter.shortConverter(value)
        count = messenger.send(testpack)
        print('Sent %s bytes' % testpack)
        pycom.heartbeat(True)
        time.sleep(0.1)
        pycom.heartbeat(False)
        time.sleep(0.4)
        i += 1