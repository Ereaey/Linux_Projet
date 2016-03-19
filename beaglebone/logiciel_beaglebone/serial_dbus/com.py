import serial
import os
import time
from protocole import *

os.system("echo BB-UART1 > /sys/devices/bone_capemgr.8/slots")
time.sleep(3)

uart = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout = None)

p = Protocole()
while 1:
    a = uart.readline()
    typeTrame = ord(a[0])
    octet1 = ord(a[1])
    octet2 = ord(a[2])
    if typeTrame == 0x44:
        if octet1 == 0x41:
            p.drawShape("square")
        elif octet1 == 0x42:
            p.drawShape("circle")
        elif octet1 == 0x43:
            p.drawShape("spiral")
    elif typeTrame == 0x43:
        if octet1 == 0x41:
            p.Laser("off")
        elif octet1 == 0x42:
            p.Laser("on")
    elif typeTrame == 0x42:
        p.moveTo(octet1 - 0x41, octet2 - 0x41)
    elif typeTrame == 0x41:
        p.moveFrom(octet1 - 0x41, octet2 - 0x41)