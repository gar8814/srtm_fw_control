import uhal
''' This class is the interface for performing read and write opartions 
    via the ipbus protocol 
'''
uhal.setLogLevelTo(uhal.LogLevel. WARNING)
class Ipbus:
    
    def __init__(self, ipAddr, debug=False):
        self._ipAddr = ipAddr
        self._manager = uhal.ConnectionManager("file://srtm_connection.xml")
        self._hw = self._manager.getDevice("atca.tcp.srtm")
        self._debug = debug
        print(debug)
        
        
    def read(self, reg):
        ''' Read a single register and retun the read value
        '''
        if (self._debug):
            print(f"I read {reg} correctly.")
            return 0xdeadbeef
        else:
            out = self._hw.getNode(reg).read()
            try:
                self._hw.dispatch()
                return out
            except: 
                print("Error reading register")
                return -1

    def write(self, reg, data):
        ''' Write to a register and return 0 if success or -1 for error. 
        '''
        if(self._debug):
            print(f"I wrote {data} to {reg}.")
            return 0
        else: 
            self._hw.getNode(reg).write(data)
            try:
                self._hw.dispatch()
                return 0
            except:
                print("Error writing register")
                return -1

