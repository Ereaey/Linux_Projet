import time
import math

import json

class Shape:
    def __init__(self, t):
        self.t = t
        self.zeroH = -90;
        self.zeroV = -90;
        #0 a 180 pour le repere
        pass
    
    def drawCircle(self):
        print "Draw circle"
        self.t.turnOnLaser()
        for nb in range(0, 5):
            for f in range(0, 360, 5):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * 25.0), int(math.sin(angle) * 25.0))
                time.sleep(0.01)
        self.t.turnOffLaser()
        
    def drawSpiral(self):
        print "Draw Spiral"
        self.t.turnOnLaser()
        for nb in range(30, 0, -3):
            for f in range(0, 360, 10):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * nb), int(math.sin(angle) * nb))
                time.sleep(0.01)
        for nb in range(0, 30, 3):
            for f in range(0, 360, 10):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * nb * -1), int(math.sin(angle) * nb))
                time.sleep(0.01)
        self.t.turnOffLaser()
                
    def moveTo(self, X, Y):
        self.t.setAngleHorizontal(X + self.zeroH)
        self.t.setAngleVertical(Y + self.zeroV)
        
    def moveFrom(self, X, Y):
        a = self.getPosition()
        self.moveTo(a[0] + X, a[1] + Y)
        
    def getPosition(self):
        return self.t.servoHorizontal.getAngle() - self.zeroH, self.t.servoVertical.getAngle() - self.zeroV
        
    def drawLine(self, posX, posY):
        X = int(self.getPosition()[0])
        Y = int(self.getPosition()[1])
        t = math.sqrt((posX - X)**2 + (posY - Y)**2)
        for i in range(0, int(math.ceil(t))):
            e = i
            if i > t:
                e = t
            self.moveTo(int(X + (posX - X) / t * e), int(Y + (posY - Y) / t * e))
            time.sleep(0.01)
            
    def drawShape(self, forme):
        json_data=open('configuration.json')
        data = json.load(json_data)
        json_data.close()
        
        for i in data["shapes"]:
            if i["shape"] == forme:
                if i.items()[1][0] == "method":
                    method = getattr(self, i.items()[1][1])
                    method()
                elif i.items()[1][0] == "file":
                    self.drawJSON(i.items()[1][1])
                    
    def drawJSON(self, file):
        json_data=open('shapes/' + file)
        data = json.load(json_data)
        json_data.close()
        self.moveTo(int(data["draw"]["originX"]), int(data["draw"]["originY"]))
        self.t.turnOnLaser()
        for i in data["draw"]["movement"]:
            if i["type"] == "line":
                self.drawLine(int(i["posX"]), int(i["posY"]))
            elif i["type"] == "moveTo":
                self.moveTo(int(i["posX"]), int(i["posY"]))
            elif i["type"] == "moveFrom":
                self.moveFrom(int(i["posX"]), int(i["posY"]))
        self.t.turnOffLaser()