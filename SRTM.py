from Ipbus import Ipbus

class SRTM:

    def __init__(self, id, debug=False):
        self.num_registers = 8
        self._id = id
        if (debug):
            self._ipbus = Ipbus('192.168.0'+id, True)
        else:
            self._ipbus = Ipbus("192.168.0." + id)

    def read_axi_board_info_efues(self):
        reg = self._ipbus.read("axi_boardinfo_efuse")

        return reg

    def read_axi_board_info_dnaHigh(self):
        reg = self._ipbus.read("axi_boardinfo_dna_high")

        return reg

    def read_axi_board_info_middle(self):
        reg = self._ipbus.read("axi_boardinfo_dna_middle")

        return reg
    
    def read_axi_board_info_low(self):
        reg = self._ipbus.read("axi_boardinfo_dna_low")

        return reg
    
    def _does_reg_exist(self, reg):
        if (isinstance(reg, int) is False):
            return False

        if (reg < 0 | reg > (self.num_registers - 1)):
            return False
        
        return True
    
    def read_axi_boardinfo_usernum(self, reg):
        # reg = corresponding register number
        #
        # @return values:
        # successful return = reg read
        # reg doesn't exist = None

        if self._does_reg_exist(reg) is False:
            return None
        
        reg_name = "axi_boardinfo_user_reg" + str(reg)
        reg = self._ipbus.read(reg_name)

        return reg
        
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
