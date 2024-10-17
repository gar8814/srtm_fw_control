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
        while (True):
            command = self._menu.run()
            #if menu.run returns null, maybe change to -1, then end
            if command==None:
                break
            else:
                if command=='axi_boardinfo_efuse':
                    for srtm in self._srtms:
                        print(hex(srtm.read_axi_board_info_efues()))
                elif command=='axi_boardinfo_dna_low':
                    #for srtm in self._srtms:
                    #  print(hex(srtm.read_axi_board_info_dnaLow()))
                    pass
                elif command=='axi_boardinfo_dna_middle':
                    #for srtm in self._srtms:
                    #  print(hex(srtm.read_axi_board_info_dnaMiddle()))
                    pass
                elif command=='axi_boardinfo_dna_high':
                    for srtm in self._srtms:
                      print(hex(srtm.read_axi_board_info_dnaHigh()))
                elif command=='axi_boardinfo_user_reg0':
                    pass
                elif command=='axi_boardinfo_user_reg1':
                    pass
                elif command=='axi_boardinfo_user_reg2':
                    pass
                elif command=='axi_boardinfo_user_reg3':
                    pass
                elif command=='axi_boardinfo_user_reg4':
                    pass
                elif command=='axi_boardinfo_user_reg5':
                    pass
                elif command=='axi_boardinfo_user_reg6':
                    pass
                elif command=='axi_boardinfo_user_reg7':
                    pass
                elif command=='freq_count_ctrl_reg':
                    pass
                elif command=='freq_count_max_cnt':
                    pass
                elif command=='freq_count_base':
                    pass
                elif command=='freq_count_clk0':
                    pass
                elif command=='freq_count_clk1':
                    pass
                elif command=='freq_count_clk2':
                    pass
                elif command=='freq_count_clk3':
                    pass
                elif command=='freq_count_clk4':
                    pass
                elif command=='freq_count_clk5':
                    pass
                elif command=='freq_count_clk6':
                    pass
                elif command=='freq_count_clk7':
                    pass
                elif command=='freq_count_clk8':
                    pass
                elif command=='freq_count_clk9':
                    pass
                elif command=='freq_count_clk10':
                    pass
                elif command=='freq_count_clk11':
                    pass
                elif command=='freq_count_clk12':
                    pass
                elif command=='freq_count_clk13':
                    pass
                elif command=='freq_count_clk14':
                    pass
                elif command=='freq_count_clk15':
                    pass
                elif command=='freq_count_clk16':
                    pass
                #expand as SRTM is more complete

