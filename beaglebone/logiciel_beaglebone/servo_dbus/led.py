from gpio import *

class Led:
    def __init__(self, pin):
        self.pin = pin
        self.gpio = GPIO()
        self.gpio.create(pin)
        self.gpio.outputPin(pin)
        self.gpio.setValue(self.pin, 0)
        pass
    
    def turnOn(self):
        self.gpio.setValue(self.pin, 1)
        pass
    
    def turnOff(self):
        self.gpio.setValue(self.pin, 0)
        pass
