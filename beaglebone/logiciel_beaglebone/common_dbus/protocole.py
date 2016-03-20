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
        
    def treatment(data):
        typeTrame = ord(data[0])
        octet1 = ord(data[1])
        octet2 = ord(data[2])
        if typeTrame == 0x44:
            if octet1 == 0x41:
                self.drawShape("square")
            elif octet1 == 0x42:
                self.drawShape("circle")
            elif octet1 == 0x43:
                self.drawShape("spiral")
        elif typeTrame == 0x43:
            if octet1 == 0x41:
                self.Laser("off")
            elif octet1 == 0x42:
                self.Laser("on")
        elif typeTrame == 0x42:
            self.moveTo(octet1 - 0x41, octet2 - 0x41)
        elif typeTrame == 0x41:
            self.moveFrom(octet1 - 0x41, octet2 - 0x41)