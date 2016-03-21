from servo import *
from shape import *
from led import *
import pwm

import json

class Turret:
    def __init__(self):
        pwm.enablePWM()
        
        json_data=open('/home/debian/logiciel_beaglebone/servo_dbus/configuration.json')
        data = json.load(json_data)
        json_data.close()
        
        self.servoHorizontal = Servo(data["configuration"]["servoHorizontal"])
        self.servoVertical = Servo(data["configuration"]["servoVertical"])
        self.laser = Led(int(data["configuration"]["laser"]))#P8_14
        self.modeShape = Led(int(data["configuration"]["ledmode"]))
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
        self.modeShape.turnOn()
        self.shape.drawShape(forme)
        self.modeShape.turnOff()
     
    def turnOnLaser(self):
        self.laser.turnOn()
    
    def turnOffLaser(self):
        self.laser.turnOff()
        

#t = Turret()
#t.draw("square")
