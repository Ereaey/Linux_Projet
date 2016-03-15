import os
import time

class PWM:
    def __init__(self):
        os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.8/slots")
        
    def set_duty(self, channel, duty):
        n = self.getNameChannel(channel)
        os.system("echo " + str(duty) + " > /sys/devices/ocp.3/"+n+"/duty")
    
    def set_period(self, channel, period):
        n = self.getNameChannel(channel)
        os.system("echo " + str(period) + " > /sys/devices/ocp.3/"+n+"/period")
    
    def set_polarity(self, channel, polarity):
        n = self.getNameChannel(channel)
        os.system("echo " + str(polarity) + " > /sys/devices/ocp.3/"+n+"/polarity")
    
    def start(self, channel, duty, period):
        os.system("echo bone_pwm_"+channel+" > /sys/devices/bone_capemgr.8/slots")
        time.sleep(2)
        n = self.getNameChannel(channel)
        os.system("echo " + str(duty) + " > /sys/devices/ocp.3/"+n+"/duty")
        os.system("echo " + str(period) + " > /sys/devices/ocp.3/"+n+"/period")
        time.sleep(0.1)
        os.system("echo 1 > /sys/devices/ocp.3/"+n+"/run")
        
    def getNameChannel(self, channel):
        name = os.popen("ls /sys/devices/ocp.3 | grep pwm_test_"+channel)
        return name.read()[:-1]
        
#p = PWM()
#p.start("P8_13", 25000, 20000000)
#p.set_duty("P8_13", 12500)
#p.set_polarity(1)