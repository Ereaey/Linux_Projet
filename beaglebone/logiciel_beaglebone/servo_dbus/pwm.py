import os
import time

def enablePWM():
    os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.8/slots")
    time.sleep(2)

def writeFile(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()

def readFile(file):
    f = open(file, 'r')
    data = f.read()
    f.close()
    return data
    
class PWM:
    def __init__(self, channel, duty, period):
        os.system("echo bone_pwm_"+channel+" > /sys/devices/bone_capemgr.8/slots")
        time.sleep(2)
        self.name = self.getNameChannel(channel)
        os.system("echo " + str(period) + " > /sys/devices/ocp.3/"+self.name+"/period")
        os.system("echo " + str(duty) + " > /sys/devices/ocp.3/"+self.name+"/duty")
        time.sleep(1)
        writeFile("/sys/devices/ocp.3/"+self.name+"/run", str(1))
        
    def set_duty(self, duty):
        writeFile("/sys/devices/ocp.3/"+self.name+"/duty", str(duty))

    def set_period(self, period):
        writeFile("/sys/devices/ocp.3/"+self.name+"/period", str(period))

    def set_polarity(self, polarity):
        writeFile("/sys/devices/ocp.3/"+self.name+"/polarity", str(polarity))
        
    def get_duty(self):
        return readFile("/sys/devices/ocp.3/"+self.name+"/duty")
        
    def get_period(self):
        return readFile("/sys/devices/ocp.3/"+self.name+"/period")

    def getNameChannel(self, channel):
        name = os.popen("ls /sys/devices/ocp.3 | grep pwm_test_"+channel)
        return name.read()[:-1]
       
'''
p = PWM()
p.start("P8_13", 25000, 20000000)
p.set_duty(12500)
p.set_polarity(1)
'''