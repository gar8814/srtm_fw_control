from Ipbus import Ipbus
import time

class SRTM:

    def __init__(self, id, debug=False):
        self.num_registers = 8
        self._id = id
        if (debug):
            self._ipbus = Ipbus('192.168.0'+id, True)
        else:
            self._ipbus = Ipbus("192.168.0." + id)

    def read_board(self, reg):
        # returns None for invalid reg values
        if reg == "efuse":
            return self._ipbus.read("axi_boardinfo_efuse")
        if reg == "high":
            return self._ipbus.read("axi_boardinfo_dna_high")
        if reg == "middle":
            return self._ipbus.read("axi_boardinfo_dna_middle")
        if reg == "low":
            return self._ipbus.read("axi_boardinfo_dna_low")
        if isinstance(reg, int):
            if(reg< 0 | reg > (self.num_registers - 1)):
                return None
            reg_name = "axi_boardinfo_user_reg" + str(reg)
            return self._ipbus.read(reg_name)
        return None
        
    def write_axi_boardinfo_usernum(self, reg, write):
        # Attempts to write to register
        # 
        # @return values:
        # successful return = 0
        # write failure = -1
        # register is read only = -2
        # register doesn't exist = -3

        if self._does_reg_exist is False:
            return -3

        if reg < 5:
            return -2
        
        reg_name = "axi_boardinfo_user_reg" + str(reg)
        wri = self._ipbus.write(reg_name, write)
        
        return wri
    
    # Reads (and prints) all boards
    def read_all_boards(self):
        efuse = self.read_board("efuse")
        print(f'efuse:      {efuse}')

        high = self.read_board("high")
        middle = self.read_board("middle")
        low = self.read_board("low")
        print(f'dna high:   {high}')
        print(f'dna middle: {middle}')
        print(f'dna low:    {low}')

        for i in range(self.num_registers):
            reg = self.read_board(i)
            print(f'userreg {i}:  {reg}')
        return
    
    def lti_send_test_data(self, case):
        try:
            f = open(f'lit_data/lti_input_data_case{case}.dat','r')
            g = open(f'lit_data/lti_input_data_case{case}.dat','r')

            wait = 0.2
            linecount = 0
            for line in f:
                linecout += 1

            print('lti reset 1')
            self._ipbus.write('lti_control_reg.reset', 1)
            time.sleep(5)

            print('lti reset 0')
            self._ipbus.write('lti_control_reg.reset', 0)
            time.sleep(5)

            print('lti loopback 0')
            self._ipbus.write("lti_control_reg.loopback", 0)
            time.sleep(wait)

            print('lti loopback 1')
            self._ipbus.write("lti_control_reg.loopback", 1)
            time.sleep(wait)

            print('lti loopback 0')
            self._ipbus.write("lti_control_reg.loopback", 0)
            time.sleep(wait)

            print('lti frame source 1')
            self._ipbus.write("lti_control_reg.frame_source", 1)
            time.sleep(wait)

            print('lti frame source 0')
            self._ipbus.write("lti_control_reg.frame_source", 0)
            time.sleep(wait)

            print('lti frame source 1')
            self._ipbus.write("lti_control_reg.frame_source", 1)
            time.sleep(wait)

            max_words = linecount
            print(f"write max_words = {max_words}")
            self._ipbus.write("lti_max_words", max_words)
            time.sleep(wait)

            print ('writing tx fifo data and charisk')
            for i in range(linecount):
                s = f.readline().split()
                lti_data = int(s[0],16)
                s = g.readline().split()
                lti_kchar = int(s[0], 16)
                self._ipbus.write("lti_tx_fifo_charisk", lti_kchar)
                time.sleep(wait)
                self._ipbus.write("lti_tx_fifo_data", lti_data)
                time.sleep(wait)
            
            print ('read tx fifo word count')
            reg0 = self._ipbus.read("lti_tx_word_cnt")
            time.sleep(wait)
            print("lti_tx_word_cnt", hex(reg0))

            print ('read rx fifo word count')
            reg0 = self._ipbus.read("lti_rx_word_cnt")
            time.sleep(wait)
            print("lti_rx_word_cnt", hex(reg0))

            print ('send to 1')
            send = 1
            self._ipbus.write("lti_control_reg.send", send)
            time.sleep(wait)

            print ('send to 0')
            send = 0
            self._ipbus.write("lti_control_reg.send", send)
            time.sleep(wait)

            print ('read tx fifo word count')
            reg0 = self._ipbus.read("lti_tx_word_cnt")
            time.sleep(wait)
            print("lti_tx_word_cnt", hex(reg0))

            print ('read rx fifo word count')
            reg0 = self._ipbus.read("lti_rx_word_cnt")
            time.sleep(wait)
            print("lti_rx_word_cnt", hex(reg0))

            f.close()
            g.close()
            print ('done!')


        except:
            print('Bad Case')
        
    def _do_lti_case_1():
        pass
