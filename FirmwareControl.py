from SRTM import SRTM
from Menu import Menu


class FirmwareControl:
    def __init__(self, debug=False):
        self._srtms = []
        self._srtms.append(SRTM("117", debug))
        self._menu = Menu()

    def getReadWrite(self):
        ret = 0
        while (ret < 1 or ret > 2):
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
            if command == 0:
                break
            elif command == "Read Board Info":
                self.handleReadBoardInfo()

            elif command == "Read Frequency Counter":
                self.handleReadFreqCounter()

            elif command == "Run Test A":
                self.handleLTITestA()

            elif command == "Run Test B":
                self.handleLTITestB()
            # returns reg name
            elif command == 'freq_count_max_cnt':
                self.handleFreqMaxCount(command)
            else:
                self.handleWriteBoardInfo(command)

    def handleReadBoardInfo(self):
        for i in range(len(self._srtms)):
            self._srtms[i].read_all_boards()

    def handleReadFreqCounter(self):
        for i in range(len(self._srtms)):
            self._srtms[i].read_all_clk()

    def handleLTITestA(self):
        case = self.LTIcase()
        print(f'LTI {case} runs here')
        for i in range(len(self._srtms)):
            self._srtms[i].lti_send_test_data(case)

    def handleWriteBoardInfo(self, command):
        msg = self.writeMsg()
        for i in range(len(self._srtms)):
            self._srtms[i].write_axi_boardinfo_usernum(command, msg)

    def handleLTITestB(self):
        case = self.LTIcase()
        print(f'LTI {case} runs here')
        # SRTM.lti_send_test_data(case)

    def handleFreqMaxCount(self, command):
        print("INFO: ")
        if self.getReadWrite() == 1:
            msg = self.writeMsg()
            for i in range(len(self._srtms)):
                self._srtms[i].write_axi_boardinfo_usernum(command, msg)
