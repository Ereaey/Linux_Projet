#!/usr/bin/python

import dbus
import dbus.service
import dbus.mainloop.glib

import gobject
import json
from turret import *

class Service(dbus.service.Object):
    def __init__(self, message):
        self._message = message
    
    def run(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus_name = dbus.service.BusName("com.turret.test", dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, "/com/turret/test")
        self.t = Turret()
        self._loop = gobject.MainLoop()
        print "Service running..."
        self._loop.run()
        print "Service stopped"

    @dbus.service.method("com.turret.test", in_signature='s', out_signature='')
    def draw(self, shape):
        self.t.draw(shape)
        
    @dbus.service.method("com.turret.test", in_signature='ss', out_signature='')
    def moveTo(self, x, y):
        self.t.shape.moveTo(int(x), int(y))
        
    @dbus.service.method("com.turret.test", in_signature='', out_signature='')
    def reset(self):
        self.t.shape.moveTo(90, 90)
    
    @dbus.service.method("com.turret.test", in_signature='ss', out_signature='')
    def moveFrom(self, X, Y):
        self.t.shape.moveFrom(int(X), int(Y))
    
    @dbus.service.method("com.turret.test", in_signature='s', out_signature='')
    def led(self, value):
        if value == "on":
            self.t.turnOnLaser()
        elif value == "off":
            self.t.turnOffLaser()
        
    @dbus.service.method("com.turret.test", in_signature='', out_signature='')
    def quit(self):
        self._loop.quit()

if __name__ == "__main__":
   Service("Demarrage de la tourelle").run()