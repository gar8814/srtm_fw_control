from FirmwareControl import FirmwareControl
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', default=False, help='Use fake ipbus')
    parser.add_argument('-S', '--subsystem', help='Select subsystem to command ie, "AXI_BOARD_INFO, FEQ, LTI, SPI')
    parser.add_argument('-c', '--command', help='Select the command to be run ie, "READ, RUN ')
    args = parser.parse_args()
    instance = FirmwareControl(args.debug)
    instance.run()

if __name__ == "__main__":
    main()
