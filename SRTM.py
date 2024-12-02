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
    
    def read_all_clk(self, max_count=100000000):

        nclks = self._ipbus.read('freq_count_ctrl_reg.freq_count_nclks')
        print(f'nClks (as set by Firmware): {int(nclks)}')

        maxCnt = self._ipbus.read("freq_count_max_cnt")
        print(f'Default Max_Cnt (as set by Firmware): {int(maxCnt)}')

        self._ipbus.write("freq_count_max_cnt", max_count)

        maxCnt = self._ipbus.read("freq_count_max_cnt")
        print(f'After write Max_Cnt (as set by Firmware): {int(maxCnt)}')

        # See what done is as test
        done = self._ipbus.read("freq_count_ctrl_reg.freq_count_done")
        print (f'done test: {hex(done)}')

        # Initial condition set enable to 0 
        enable = 0
        self._ipbus.write("freq_count_ctrl_reg.freq_count_enable", enable)
        print('writing enable bit = 0')

        en_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_clear")
        print (f'enable set to: {hex(en_r)}')

        # clear the counters 
        clear = 1
        self._ipbus.write("freq_count_ctrl_reg.freq_count_clear", clear)
        print('writing clear bit = 1')

        clear_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_clear")
        print (f'clear set to: {hex(clear_r)}')

        # set clear to back to 0
        clear = 0
        self._ipbus.write("freq_count_ctrl_reg.freq_count_clear", clear)
        print('writing clear bit = 0')

        clear_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_clear")
        print (f'clear set to: {hex(clear_r)}')

        # See done should be 0
        done = self._ipbus.read("freq_count_ctrl_reg.freq_count_done")
        print (f'done test: {hex(done)}')

        # enable the counters
        enable = 1
        self._ipbus.write("freq_count_ctrl_reg.freq_count_enable", enable)
        print('writing enable bit = 1')

        en_r = self._ipbus.read("freq_count_ctrl_reg.freq_count_enable")
        print (f'enable set to: {hex(en_r)}')

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


        ### Read the count values and find associated frequencies
        freqB = self._ipbus.read("freq_count_base")
        # print (type(freqB))
        # print (freqB)
        print(f'Base clk:         {int(freqB)}')


        freq0 = self._ipbus.read("freq_count_clk0")
        print(f'clk 0 gbe1_clk 229 1(U5-QP0):                     {int(freq0)}')

        freq1 = self._ipbus.read("freq_count_clk1")
        # print (type(freq1))
        print(f'clk 1 axi_clk_in (kj_125M) 65 (U5-QP2):           {int(freq1)}')
        #print('clk 1: ', freq1, ' frequency of ', 100*float(freq1)/float(freq0))

        freq2 = self._ipbus.read("freq_count_clk2")
        print(f"clk 2 xaui clk 229 0 (U3):                        {int(freq2)}")

        freq3 = self._ipbus.read("freq_count_clk3")
        print(f"clk 3 tdaq1_refclk0 128 0 (U27-OUT1):             {int(freq3)}")

        freq4 = self._ipbus.read("freq_count_clk4")
        print(f"clk 4 tdaq2_refclk0 129 0 (U27-OUT2):             {int(freq4)}")

        freq5 = self._ipbus.read("freq_count_clk5")
        print(f"clk 5 tdaq3_refclk0 130 0 (U27-OUT3):             {int(freq5)}")

        freq6 = self._ipbus.read("freq_count_clk6")
        print(f"clk 6 tdaq4_refclk0 131 (U27-OUT4):               {int(freq6)}")

        freq7 = self._ipbus.read("freq_count_clk7")
        print(f"clk 7 si5395_0_out6 65 (U27-OUT6):                {int(freq7)}")

        freq8 = self._ipbus.read("freq_count_clk8")
        print(f"clk 8 si5395_0_out7 (40 MHz TTC) (U27-OUT7):      {int(freq8)}")

        freq9 = self._ipbus.read("freq_count_clk9")
        print(f"clk 9 tdaq1_refclk1 128 (U32-OUT1):               {int(freq9)}")

        freq10 = self._ipbus.read("freq_count_clk10")
        print(f"clk 10 tdaq2_refclk1 129 1 (U32-OUT2):            {int(freq10)}")

        freq11 = self._ipbus.read("freq_count_clk11")
        print(f"clk 11 tdaq3_refclk1 130 1 (U32-OUT3):            {int(freq11)}")

        freq12 = self._ipbus.read("freq_count_clk12")
        print(f"clk 12 tdaq4_refclk1 131 1 (U32-OUT4):            {int(freq12)}")

        freq13 = self._ipbus.read("freq_count_clk13")
        print(f"clk 13 si5395_1_out6 65 (U32-OUT6):               {int(freq13)}")

        freq14 = self._ipbus.read("freq_count_clk14")
        print(f"clk 14 si5395_1_out7 (40 MHz TTC alt) (U32-OUT7): {int(freq14)}")

        freq15 = self._ipbus.read("freq_count_clk15")
        print(f"clk 15 ext_strobe (Zone3):                        {int(freq15)}")

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
        print(f'INFO: entered SRTM.lti_send_test_data({case})')
        print(f'INFO: ATTEMPTING TO OPEN:')
        print(f'lti_data/lti_input_data_case{case}.dat')
        print(f'lti_data/lti_input_txctrl2_case{case}.dat')
        try:
            print('INFO: Opening file')
            f = open(f'lti_data/lti_input_data_case{case}.dat','r')
            g = open(f'lti_data/lti_input_txctrl2_case{case}.dat','r')

            print('INFO: File Open!')
            wait = 0.2
            linecount = 0
            for line in f:
                linecount += 1
            f.close()
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
            if (case == 2):
                print('This can take ~10min')
                0
            f = open(f'lti_data/lti_input_data_case{case}.dat','r')
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


        except Exception as error:
            print('Bad Case: ', error)
        
    def spi_send_data_master(self):
        print('spi data sent from master')

    def spi_read_sanity(self):
        print('reading sanity')
        reg0 = self._ipbus.read("spi_sanity_reg")
        print("spi sanity register = ", hex(reg0))

        print('done!')


    def spi_read_status(self):
        print('reading status')
        wait = 0.25

        #print ('read spi master status')
        print (' ')
        reg0 = self._ipbus.read("spi_master_status_reg.master_ready")
        time.sleep(wait)
        print("spi master_ready", hex(reg0))

        #print ('read spi slave status')                                                                                                                               
        print (' ')
        reg0 = self._ipbus.read("spi_slave_status_reg.slave_ready")
        time.sleep(wait)
        print("spi slave_ready", hex(reg0))

        print ('done!')

    
    def spi_send_reset(self):
        print('sent reset')