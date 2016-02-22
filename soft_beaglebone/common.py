#http://elinux.org/BeagleBone_Community#BeagleBone_.28original.29
#http://derekmolloy.ie/gpios-on-the-beaglebone-black-using-device-tree-overlays/
#activer devicetree
#tab, name, key, pin

class BeagleBone:
    def __init__(self):
        self.nbdevice = 10;
        self.pins = [[0] * 3 for _ in range(self.nbdevice)]
    
    def get_key_by_name(self, name):
        pass
    
    def get_pin_by_name(self, name):
        pass
    
    def get_key_by_pin(self, pin):
        pass
    
    def get_name_by_pin(self, pin):
        pass
    
    def get_pin_by_key(self, key):
        pass
    
    def get_name_by_key(self, key):
        pass
    
