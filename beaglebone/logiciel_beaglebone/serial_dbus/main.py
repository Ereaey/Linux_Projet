import serial
import os
import time
from common_dbus/protocole import *

os.system("echo BB-UART1 > /sys/devices/bone_capemgr.8/slots")
time.sleep(3)

uart = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout = None)

p = Protocole()
while 1:
    a = uart.readline()
    treatment(a)