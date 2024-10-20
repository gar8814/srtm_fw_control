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
    
    def run(self):
        # while (True):
        #     print("SRTM Firmware Control:")
        #     print("1. Read Board Info DNA High")
        #     usr_input = input("Select an option:(0 to exit)")
        #     if usr_input == '0':
        #         break
        #     else:
        #         for srtm in self._srtms:
        #             print(hex(srtm.read_axi_board_info_dnaHigh()))
        
        

        while (True):
            command = self._menu.run()
            #if menu.run returns null, maybe change to -1, then end
            if command==0:
                break
            else:
                    if command=='axi_boardinfo_efuse':
                        for srtm in self._srtms:
                            print(hex(srtm.read_axi_board_info_efues()))
                    elif command=='axi_boardinfo_dna_low':
                        for srtm in self._srtms:
                          print(hex(srtm.read_axi_board_info_low()))
                        pass
                    elif command=='axi_boardinfo_dna_middle':
                        for srtm in self._srtms:
                          print(hex(srtm.read_axi_board_info_middle()))
                        pass
                    elif command=='axi_boardinfo_dna_high':
                        for srtm in self._srtms:
                             print(hex(srtm.read_axi_board_info_dnaHigh()))
                    elif command=='axi_boardinfo_user_reg0':
                        for srtm in self._srtms:
                            print(hex(srtm.read_axi_boardinfo_usernum(0)))
                    elif command=='axi_boardinfo_user_reg1':
                        for srtm in self._srtms:
                            print(hex(srtm.read_axi_boardinfo_usernum(1)))
                    elif command=='axi_boardinfo_user_reg2':
                        for srtm in self._srtms:
                            print(hex(srtm.read_axi_boardinfo_usernum(2)))
                    elif command=='axi_boardinfo_user_reg3':
                        for srtm in self._srtms:
                            print(hex(srtm.read_axi_boardinfo_usernum(3)))
                    elif command=='axi_boardinfo_user_reg4':
                        for srtm in self._srtms:
                            print(hex(srtm.read_axi_boardinfo_usernum(4)))
                    elif command=='axi_boardinfo_user_reg5':
                        if self.getReadWrite()==1:
                            for srtm in self._srtms:
                                print(hex(srtm.read_axi_boardinfo_usernum(5)))
                        else:
                            for srtm in self._srtms:
                                print(hex(srtm.write_axi_boardinfo_usernum(5)))
                    elif command=='axi_boardinfo_user_reg6':
                        if self.getReadWrite()==1:
                            for srtm in self._srtms:
                                print(hex(srtm.read_axi_boardinfo_usernum(6)))
                        else:
                            for srtm in self._srtms:
                                print(hex(srtm.write_axi_boardinfo_usernum(6)))
                    elif command=='axi_boardinfo_user_reg7':
                        if self.getReadWrite()==1:
                            for srtm in self._srtms:
                                print(hex(srtm.read_axi_boardinfo_usernum(7)))
                        else:
                            for srtm in self._srtms:
                                print(hex(srtm.write_axi_boardinfo_usernum(7)))
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
