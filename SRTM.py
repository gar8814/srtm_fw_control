from Ipbus import Ipbus

class SRTM:
    def __init__(self, id):
        self._id = id
        self._ipbus = Ipbus("192.168.0." + id)

    def read_axi_board_info_efues(self):
        reg = self._ipbus.read("axi_boardinfo_efuse")

        return reg

    def read_axi_board_info_dnaHigh(self):
        reg = self._ipbus.read("axi_boardinfo_dna_high")

        return reg
