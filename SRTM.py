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
    

    def write_then_read_clear_node(self, clearbit):
        self._ipbus.write("freq_count_ctrl_reg.freq_count_enable", 0)
        print("Writing enable bit = 0")
        en_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_enable")
        print (f'enable set to: {hex(en_r)}')
        return
    
    def _read_each_clk(self):
        clk_names = ["(U5-QP0)", "(U5-QP2)", "(U3)", "(U27-OUT1)",
                     "(U27-OUT2)", "(U27-OUT3)", "(U27-OUT4)", "(U27-OUT6)",
                     "(U27-OUT7)", "(U32-OUT1)", "(U32-OUT2)" "(U32-OUT3)",
                     "(U32-OUT4)", "(U32-OUT6)", "(U32-OUT7)", "(Zone3)"]
        # Read the count values and find associated frequencies
        freqB = self._ipbus.read("freq_count_base")
        print(f'Base clk:         {int(freqB)}')

        for i in range(15):
            name_of_clock = "freq_count_clk" + str(i)
            freq = self._ipbus.read(name_of_clock)
            whitespace_amount = " " * (13 - len(clk_names[i]))
            print(f'clk {i}{clk_names[i]}:{whitespace_amount}{int(freq)}')

        print ('freq0: gbe1_clk 229 1')
        print ('freq1: axi_clk_in (kj_125M) 65 x')
        print ('freq2: xaui clk 229 0')
        print ('freq3: tdaq1_refclk0 128 0')
        print ('freq4: tdaq2_refclk0 129 0')
        print ('freq5: tdaq3_refclk0 130 0')
        print ('freq6: tdaq4_refclk0 131 0')
        print ('freq7: si5395_0_out6 65 x')
        print ('freq8: si5395_0_out7 (40 MHz TTC) 65 x')
        print ('freq9: tdaq1_refclk1 128 1')
        print ('freq10: tdaq2_refclk1 129 1')
        print ('freq11: tdaq3_refclk1 130 1')
        print ('freq12: tdaq4_refclk1 131 1')
        print ('freq13: si5395_1_out6 65 x')
        print ('freq14: si5395_1_out7 (40 MHz TTC alt) 65 x')
        print ('freq15: ext_strobe 71 X')


        clear = 1
        self._ipbus.write("freq_count_ctrl_reg.freq_count_clear", clear)
        print("writing clear bit: ", clear)

        read_clear = self._ipbus.read("freq_count_ctrl_reg.freq_count_clear")
        print("clear: ", hex(read_clear))
        return
    
    def _clear_counters(self):
        # Initial condition set enable to 0
        self._ipbus.write("freq_count_ctrl_reg.freq_count_enable", 0)
        print("Writing enable bit = 0")
        en_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_enable")
        print (f'enable set to: {hex(en_r)}')

        # Clear counters
        self._ipbus.write("freq_count_ctrl_reg.freq_count_clear", 1)
        print("Writing clear bit = 1")
        clear_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_clear")
        print (f'enable set to: {hex(clear_r)}')

        # Set clear back to 0
        self._ipbus.write("freq_count_ctrl_reg.freq_count_clear", 0)
        print("Writing clear bit = 0")
        clear_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_clear")
        print (f'enable set to: {hex(clear_r)}')

        # See done should be 0
        done = self._ipbus.read("freq_count_ctrl_reg.freq_count_done")
        print(f'done test: {hex(done)}')

        # Re-enable the counters
        self._ipbus.write("freq_count_ctrl_reg.freq_count_enable", 1)
        print("Writing clear bit = 1")
        clear_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_enable")
        print (f'enable set to: {hex(clear_r)}')
        return
    
    def clock_counter(self):
        max_count = 100000000

        # Print num of clocks
        nclks = self._ipbus.read("freq_count_ctrl_reg.freq_count_nclks")
        print(f'nClks (as set by Firmware): {int(nclks)}')

        # Print value of max counts
        max_cnt = self._ipbus.read("freq_count_max_cnt")
        print(f'Default Max_Cnt (as set by Firmware): {int(max_cnt)}')

        # Write to max counts
        self._ipbus.write("freq_count_max_cnt", max_count)
        afterwrite_max_cnt = self._ipbus.read("freq_count_max_cnt")
        print(f'After write Max_Cnt (as set by Firmware): {int(afterwrite_max_cnt)}')

        # See what is done as a test
        done = self._ipbus.read("freq_count_ctrl_reg.freq_count_done")
        print(f'done test: {hex(done)}')

        # Clear counters
        self._clear_counters()
        
        ### Wait until the done bit is set to 1
        done = self._ipbus.read("freq_count_ctrl_reg.freq_count_done")

        i = 0
        while int(hex(done),16) == 0:
            time.sleep(1)
            done = self._ipbus.read("freq_count_ctrl_reg.freq_count_done")
            i = i + 1
            if i > 10: 
                print('timeout ', i, ' seconds have passed')
                exit(1)
        print('done: ', hex(done))

        self._read_each_clk()
        return

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
