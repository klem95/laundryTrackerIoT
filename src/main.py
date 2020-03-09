
import pycom
import time
import machine
import networkSetup
import packageConverter


messenger = networkSetup.linkup() # Sending Object

off = 0x000000
green = 0x00ff00
blue = 0x0000ff

adc = machine.ADC()           # create an ADC object
apin = adc.channel(pin='P17') # Listening to Pin 17

sampleFrq = 10
sampleCount = 0
vibrations = 0

while True:
    try:
        if messenger is not None:
            vibrationValue = apin()
            vibrations += vibrationValue
            if sampleCount > sampleFrq:
                movingAvarage = int(vibrations / sampleFrq)
                package = packageConverter.shortConverter(movingAvarage)
                pycom.rgbled(blue)
                messenger.send(package)
                pycom.rgbled(off)
                sampleCount = 0
                vibrations = 0
            sampleCount += 1
            pycom.rgbled(green)
            time.sleep(0.05)
            pycom.rgbled(off)
            time.sleep(0.05)
        pass
    except Exception as e:
        print(e)
        pass
    