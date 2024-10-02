from SRTM import SRTM
from Menu import Menu

class FirmwareControl:
    def __init__(self):
        self._srtms = []
        self._srtms.append(SRTM("117"))
        self._menu = Menu()
        
        pass
    
    
    def run(self):
        while (True):
            print("SRTM Firmware Control:")
            print("1. Read Board Info DNA High")
            usr_input = input("Select an option:(0 to exit)")
            if usr_input == '0':
                break
            else:
                for srtm in self._srtms:
                    print(hex(srtm.read_axi_board_info_dnaHigh()))
        
        print("Exiting...")

