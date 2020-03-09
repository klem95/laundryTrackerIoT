import binascii
import pycom
import socket
import time
from network import LoRa


def linkup ():
    # Colors
    off = 0x000000
    red = 0xff0000
    green = 0x00ff00
    blue = 0x0000ff

    # Turn off heartbeat LED
    pycom.heartbeat(False)

    # Initialize LoRaWAN radio
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # Set network keys
    app_eui = binascii.unhexlify('70B3D57ED002B8EE')
    app_key = binascii.unhexlify('520EFBD75F227E786B091602CBCB2232')

    # Join the network
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    pycom.rgbled(green)

    # Loop until joined
    while not lora.has_joined():
        print('Not joined yet...')
        pycom.rgbled(off)
        time.sleep(0.1)
        pycom.rgbled(red)
        time.sleep(2)

    print('Joined')
    pycom.rgbled(blue)

    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    return s