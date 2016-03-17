import time
import math

class Shape:
    def __init__(self, t):
        self.t = t
        pass
    
    def drawCircle(self):
        print "Draw circle"
        for nb in range(0, 5):
            for f in range(0, 360, 4):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * 25.0), int(math.sin(angle) * 25.0))
                time.sleep(0.01)
                
    def drawSquare(self):
        print "Draw square"
        for nb in range(0, 5):
            self.t.setAngle(-25, -25)
            for i in range(-25, 26, 1):
                self.t.setAngleVertical(i)
                time.sleep(0.01)
            for i in range(-25, 26, 1):
                self.t.setAngleHorizontal(i)
                time.sleep(0.01)
            for i in range(25, -26, -1):
                self.t.setAngleVertical(i)
                time.sleep(0.01)
            for i in range(25, -26, -1):
                self.t.setAngleHorizontal(i)
                time.sleep(0.01)

'''
e = Shape("dqsd")
e.drawCircle()
'''