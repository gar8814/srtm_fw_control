from Ipbus import Ipbus

class SRTM:
    def __init__(self, id, debug=False):
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
