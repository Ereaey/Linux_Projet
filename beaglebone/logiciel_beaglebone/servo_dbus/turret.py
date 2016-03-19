from servo import *
from shape import *
from led import *
import pwm

class Turret:
    def __init__(self):
        pwm.enablePWM()
        self.servoHorizontal = Servo("P9_14")
        self.servoVertical = Servo("P8_13")
        self.laser = Led(26)#P8_14
        self.modeShape = Led(46)
        self.shape = Shape(self)
        
    def setAngle(self, angleVertical, angleHorizontal):
        self.servoVertical.setAngle(angleVertical)
        self.servoHorizontal.setAngle(angleHorizontal)
    
    def setAngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.setAngle(angleHorizontal)
    
    def setAngleVertical(self, angleVertical):
        self.servoVertical.setAngle(angleVertical)
    
    def addAngleVertical(self, angleVertical):
        self.servoVertical.setAngle(angleVertical + self.servoVertical.getAngle())

    def addAngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.setAngle(angleHorizontal + self.servoHorizontal.getAngle())

    def draw(self, forme):
        self.turnOnLaser()
        self.modeShape.turnOn()
        if forme == "square":
            self.shape.drawSquare()
        elif forme == "circle":
            self.shape.drawCircle()
        elif forme == "spiral":
            self.shape.drawSpiral()
        self.modeShape.turnOff()
        self.turnOffLaser()
            
    def turnOnLaser(self):
        self.laser.turnOn()
    
    def turnOffLaser(self):
        self.laser.turnOff()