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

    def LTIcase(self):
        print("Enter case number")
        ret = input(">").strip()
        return ret

    def run(self):
        while (True):
            command = self._menu.run()
            if command==0:
                break
            elif command=="Read Board Info":
                SRTM.read_all_boards()
            elif command=="Read Frequency Counter":
                SRTM._read_each_clk()
            elif command=="Run Test A":
                case = self.LTIcase()
                print(f'LTI {case} runs here')
            elif command=="Run Test B":
                case = self.LTIcase()
                print(f'LTI {case} runs here')
            else:
                #returns reg name
                if command == 'freq_count_max_cnt':
                    pass
                elif self.getReadWrite()==1:
                    msg=self.writeMsg()
                    SRTM.write_axi_boardinfo_usernum(command,msg)