import uhal
''' This class is the interface for performing read and write opartions 
    via the ipbus protocol 
'''
class Ipbus:
    def __init__(self, ipAddr):
        self._manager = uhal.ConnectionManager("file://srtm_connection.xml")
        self._hw = self._manager.getDevice("udp.srtm")
        
    def read(self, reg):
        ''' Read a single register and retun the read value
        '''
        out = self._hw.getNode(reg)
        self._hw.dispatch()
        return out

    def write(self, reg):
        # TODO: implment this. 
        pass 