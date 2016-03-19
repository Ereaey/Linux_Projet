import dbus

class Protocole():
    def __init__(self):
        self.bus = dbus.SessionBus()
        self.service = self.bus.get_object('com.turret.test', "/com/turret/test")
        #self._message = service.get_dbus_method('get_message', 'com.turret.service.Draw')
        #self._quit = service.get_dbus_method('quit', 'com.example.service.Quit')
        
    def drawShape(self, shape):
        self.service.draw(shape, dbus_interface = 'com.turret.test')
        
    def moveFrom(self, X, Y):
        self.service.moveFrom(X, Y, dbus_interface = 'com.turret.test')
        
    def moveTo(self, X, Y):
        self.service.moveTo(X, Y, dbus_interface = 'com.turret.test')
        
    def Laser(self, mode):
        self.service.Laser(mode, dbus_interface = 'com.turret.test')