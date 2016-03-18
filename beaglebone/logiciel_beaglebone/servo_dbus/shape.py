import time
import math

class Shape:
    def __init__(self, t):
        self.t = t
        self.zeroH = -90;
        self.zeroV = -90;
        #0 a 180 pour le repere
        pass
    
    def drawCircle(self):
        print "Draw circle"
        for nb in range(0, 5):
            for f in range(0, 360, 5):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * 25.0), int(math.sin(angle) * 25.0))
                time.sleep(0.01)
                
    def drawCircleF(self):
        print "Draw circleF"
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
                
    def moveTo(self, X, Y):
        self.t.setAngleHorizontal(X + self.zeroH)
        self.t.setAngleVertical(Y + self.zeroV)
        
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
    
    def drawSquare(self):
        print "Draw squareLine"
        for nb in range(0, 5):
            self.moveTo(75, 75)
            self.drawLine(75, 105)
            self.drawLine(105, 105)
            self.drawLine(105, 75)
            self.drawLine(75, 75)