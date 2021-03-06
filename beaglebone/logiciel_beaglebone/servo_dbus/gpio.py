import os
import time

class GPIO:
    def __init__(self):
        pass
    
    def create(self, pin):
        os.system("echo "+str(pin)+" > /sys/class/gpio/export")
        time.sleep(2)
    
    def inputPin(self, pin):
        os.system("echo in > /sys/class/gpio/gpio"+str(pin)+"/direction");
        time.sleep(0.5)
        
    def outputPin(self, pin):
        os.system("echo out > /sys/class/gpio/gpio"+str(pin)+"/direction");
        time.sleep(0.5)
        
    def setValue(self, pin, value):
        os.system("echo " + str(value) + " > /sys/class/gpio/gpio"+str(pin)+"/value");