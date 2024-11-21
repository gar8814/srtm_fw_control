from SRTM import SRTM
from Menu import Menu

class FirmwareControl:
    def __init__(self, read, debug):
        self._srtms = []
        self._srtms.append(SRTM("117", debug))
        # python can't overload functions. Since we can only work with 1 constructor
        # I think we just have to check for boolean args and perform their ops before
        # calling menu. readBoard is the example here.
        if read:
            for i in range(len(self._srtms)):
                self._srtms[i].read_all_boards()
        self._menu = Menu()

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
                for i in range(len(self._srtms)):
                    self._srtms[i].read_all_boards()
            elif command=="Read Frequency Counter":
                for i in range(len(self._srtms)):
                    self._srtms[i]._read_each_clk()
            elif command=="Run Test A":
                case = self.LTIcase()
                #print(f'LTI {case} runs here')
                for i in range(len(self._srtms)):
                    self._srtms[i].lti_send_test_data(case)
            elif command=="Run Test B":
                case = self.LTIcase()
                #print(f'LTI {case} runs here')
                for i in range(len(self._srtms)):
                    self.srtms[i].lti_send_test_data(case)
            else:
                #returns reg name
                if command == 'freq_count_max_cnt':
                    print("Max count function here")
                else:
                    msg=self.writeMsg()
                    for i in range(len(self._srtms)):
                        self._srtms[i].write_axi_boardinfo_usernum(command,msg)