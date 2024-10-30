from SRTM import SRTM
from Menu import Menu

class FirmwareControl:
    def __init__(self, debug=False):
        self._srtms = []
        self._srtms.append(SRTM("117", debug))
        self._menu = Menu()

    def getReadWrite(self):
        ret=0
        while(ret<1 or ret>2):
            print("Would you like to read (1) or write (2)?")
            ret = int(input(">").strip())
        return ret
    
    def writeMsg(self):
        print("Enter new value")
        ret = input(">").strip()
        return ret

    def run(self):
        while (True):
            command = self._menu.run()
            if command==0:
                break
            elif command=="read":
                #readAllcommand()
                #loop through dictionary or return data structure
                    #print(hex())
                pass
            elif command=="write":
                if self.getReadWrite()==1:
                    msg=self.writeMsg()
                pass
            elif command=="LTI":
                # do specified test
                pass