# test EndPoint communication 
# by sending 100 000 caracters in CDC
# Firmware coded in Arduino IDE


from multiprocessing.dummy import Array
from os import system
import re
import usb.core
import usb.util
import time
import random
import serial


serRP2040 = serial.Serial('/dev/ttyACM0',115200) # open serial port

sendToCDC = "paul\n" * 16
count = 1562
print(serRP2040.name) # print directory of serial port
print('test CDC communication')

while True:

    startCDC = time.time() # start the timer
    for i in range(count): # send packets of 64 caracters
        serRP2040.write(sendToCDC.encode()) # send to PICO
        s = serRP2040.read(len(sendToCDC)) #receive from pico

    endCDC = time.time() # stop the timer
    # serRP2040.close()
    print(f'round trip for 100000 characters in CDC is ',(endCDC - startCDC),' seconds')
