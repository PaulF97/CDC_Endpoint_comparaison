# test EndPoint communication 
# by sending 100 000 caracters and first OUT endpoint address

from multiprocessing.dummy import Array
from os import system
import re
import usb.core
import usb.util
import time
import random
import array as arr

CDC_COMM_INTF = 0
CDC_DATA_INTF = 1

# find our device
dev = usb.core.find(idVendor=0x0000, idProduct=0x0001)

# was it found?
if dev is None:
    raise ValueError('Device not found')

dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0, 0)]

outep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match= \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT)

inep = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
    custom_match= \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_IN)


assert inep is not None
assert outep is not None


count = 1563
sendToEndPoint = "Paul" * 16
print('USB Endpoint Test')

while True:

    startEDP = time.time() # start the timer
    for i in range(count): # send packets of 64 caracters
        outep.write(sendToEndPoint)  # sends hello World to first out endpoint
        from_device = inep.read(len(sendToEndPoint)) # read the response from endpoint

    endEDP = time.time() # end the timer    
    print("round trip for 100000 characters in Endpoint is ",(endEDP - startEDP)," seconds")


usb.util.dispose_resources(dev) #liberate the ressource
# system("sudo unmount /dev/bus/usb/001/024")