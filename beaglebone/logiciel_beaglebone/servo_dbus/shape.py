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
            for f in range(0, 360, 4):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * 15.0), int(math.sin(angle) * 15.0))
                time.sleep(0.01)
    
    def moveTo(self, X, Y):
        self.t.setAngle(X + self.zeroH, Y + self.zeroV)
        
    def getPosition():
        return self.t.servoHorizontal.getAngle() - self.zeroH, self.t.servoVertical.getAngle() - self.zeroV
        
    def drawLine(self, posX, posY):
        print "DrawLine"
        X = getPosition()[0]
        Y = getPosition()[1]
        print math.sqrt((posX - X)**2 + (posY - Y)**2)
        pass
        
    def drawSquare(self):
        print "Draw square"
        for nb in range(0, 5):
            self.moveTo(75, 75)
            #self.t.setAngle(-15, -15)
            for i in range(75, 106, 1):
                #self.t.setAngleVertical(i)
                self.moveTo(75, i)
                time.sleep(0.01)
            for i in range(75, 105, 1):
                #self.t.setAngleHorizontal(i)
                self.moveTo(i, 105)
                time.sleep(0.01)
            for i in range(105, 76, -1):
                #self.t.setAngleVertical(i)
                self.moveTo(105, i)
                time.sleep(0.01)
            for i in range(105, 76, -1):
                #self.t.setAngleHorizontal(i)
                time.sleep(0.01)
                self.moveTo(i, 75)

'''
e = Shape("dqsd")
e.drawCircle()
'''