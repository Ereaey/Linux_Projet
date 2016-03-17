from servo import *
from shape import *
from led import *
import pwm

class Turret:
    def __init__(self):
        pwm.enablePWM()
        self.servoHorizontal = Servo("P9_14")
        self.servoVertical = Servo("P8_13")
        self.laser = Led(60)#P8_14
        self.modeShape = Led(61)
        self.shape = Shape(self)
        
    def setAngle(self, angleVertical, angleHorizontal):
        self.servoVertical.setAngle(angleVertical)
        self.servoHorizontal.setAngle(angleHorizontal)
    
    def setAngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.setAngle(angleHorizontal)
    
    def setAngleVertical(self, angleVertical):
        self.servoVertical.setAngle(angleVertical)
        
    def draw(self, forme):
        self.modeShape.turnOn()
        if forme == "square":
            self.shape.drawSquare()
        elif forme == "circle":
            self.shape.drawCircle()
        self.modeShape.turnOff()
            
    def turnOnLaser(self):
        self.laser.turnOn()
    
    def turnOffLaser(self):
        self.laser.turnOff()
        
t = Turret()
t.draw("square")
t.draw("circle")