from pwm import *

class Servo:
    def __init__(self, channel):
        self.pwm = PWM()
        self.channel = channel
        self.pwm.start(self.channel, 1500000, 200000000)

    def setAngle(self, angle):
        if angle >= -45 or angle <= 45:
            duty = (angle + 45) * (1000000 / 90) + 1000000
            self.pwm.set_duty(self.channel, duty)

#s = Servo("P9_14", "P8_13")
#s.setAngle(12)