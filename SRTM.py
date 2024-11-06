from Ipbus import Ipbus

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