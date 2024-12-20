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
    
    def _writeMsg(self):
        print("Enter new value")
        ret = int(input(">").strip())
        return ret

    def _LTIcase(self):
        print("Enter case number")
        ret = input(">").strip()
        return ret
    
    def _getVal(self):
        print("Enter Value to Write in hex")
        ret = int(input(">").strip(), 16)
        return ret 

    def run(self):
        while (True):
            # start the menu and wait for user input. 
            command = self._menu.run()
            if command==0:
                break
            elif command=="Read Board Info":
                for i in range(len(self._srtms)):
                    self._srtms[i].read_all_boards()

            elif command=="Read Frequency Counter":
                for i in range(len(self._srtms)):
                    self._srtms[i].read_all_clk()

            elif command=="Run Test A":
                case = self._LTIcase()
                print(f'LTI {case} runs here')
                for i in range(len(self._srtms)):
                    self._srtms[i].lti_send_test_data(case)

            elif command=="Run Test B":
                case = self._LTIcase()
                print(f'LTI {case} runs here')
                #SRTM.lti_send_test_data(case)
            #returns reg name
            elif command == 'freq_count_max_cnt':
                msg=self.writeMsg()
                for i in range(len(self._srtms)):
                    self._srtms[i].write_reg(command,msg)
            elif command=="Send Master Data":
                for i in range(len(self._srtms)):
                    self._srtms[i].spi_send_data_master()
            elif command=="Read Sanity":
                for i in range(len(self._srtms)):
                    self._srtms[i].spi_read_sanity()
            elif command=="Read Status":
                for i in range(len(self._srtms)):
                    self._srtms[i].spi_read_status()
            elif command=="Send Reset":
                for i in range(len(self._srtms)):
                    self._srtms[i].spi_send_reset()
            elif command=="axi_boardinfo_user_reg5":
                for i in range(len(self._srtms)):
                    val = self._getVal()
                    ret = self._srtms[i].write_reg(command, val)
                    if ret == -1:
                        print("ERROR: Write failed")
            elif command=="axi_boardinfo_user_reg6":
                for i in range(len(self._srtms)):
                    val = self._getVal()
                    ret = self._srtms[i].write_reg(command, val)
                    if ret == -1:
                        print("ERROR: Write failed")
            elif command=="axi_boardinfo_user_reg7":
                for i in range(len(self._srtms)):
                    val = self._getVal()
                    ret = self._srtms[i].write_reg(command, val)
                    if ret == -1:
                        print("ERROR: Write failed")
            else:
                print(f'ERROR: {command} invalid:')