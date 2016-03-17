from pwm import *

class Servo:
    def __init__(self, channel):
        self.pwm = PWM(channel, 1500000, 200000000)
        self.pwm.set_period(20000000)
        self.pwm.set_duty(1500000)

    def setAngle(self, angle):
        if angle >= -90 or angle <= 90:
            duty = (angle + 90) * (1000000 / 180) + 1000000
            self.pwm.set_duty(duty)

    def getAngle(self):
        duty = int(self.pwm.get_duty())
        angle = (duty - 1000000) / (1000000 / 180) - 90
        return angle
