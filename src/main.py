import pycom
import time
import machine
import networkSetup
import packageConverter

messenger = networkSetup.linkup() # Sending Object

off = 0x000000
green = 0x00ff00

i = 0

adc = machine.ADC()           # create an ADC object
apin = adc.channel(pin='P17') # Listening to Pin 17

while True:
    try:
        if messenger is not None:
            value = apin()
            package = packageConverter.shortConverter(value)
            messenger.send(package)
            print('Sent %s bytes' % package)

            pycom.rgbled(green)
            time.sleep(0.1)
            pycom.rgbled(off)
            time.sleep(0.4)
        pass
    except Exception as e:
        print(e)
        pass
    