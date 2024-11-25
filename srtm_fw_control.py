from FirmwareControl import FirmwareControl
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', default=False, help='Use fake ipbus')
    parser.add_argument('-m', '--mode', choices=['write', 'read', 'run'], help='Mode of operation: write, read, or run')
    parser.add_argument('sub', nargs='?', default=None, help='Submenu for selecting a reg, e.g. "board" or "freq"')
    parser.add_argument('reg', nargs='?', default=None, help='Register for use in write, read, or run modes')
    parser.add_argument('series', nargs='?', default=None, help='Test series, e.g. A or B')
    args = parser.parse_args()
    instance = FirmwareControl(args.debug)
    if args.mode == 'write':
        if args.sub is None or args.reg is None:
            print("Syntax: python3 srtm_fw_control.py -m write <Subsystem> <Register>")
        else:
            if args.sub == 'board':
                instance.handleWriteBoardInfo(args.reg)
            elif args.sub == 'freq':
                instance.handleWriteFreqInfo(args.reg)
            else:
                print("Invalid write option: Try \"board\" or \"freq\".")
    elif args.mode == 'read':
        if args.sub is None or args.reg is None:
            print("Syntax: python3 srtm_fw_control.py -m read <Subsystem> <Register>")
        else:
            if args.sub.lower() == 'board':
                instance.handleReadBoardInfo()
            elif args.sub.lower() == 'freq':
                instance.handleReadFreqInfo()
            else:
                print("Invalid subsystem: Try \"board\" or \"freq\".")
    elif args.mode == 'run':
        if args.sub is None or args.reg is None or args.series is None:
            print("Syntax: python3 srtm_fw_control.py -m run <Test Unit> test <Series>")
        else:
            if args.sub.lower() == 'lti':
                if args.reg.lower() == 'test':
                    if args.series.lower() == 'a':
                        instance.handleLTITestA()
                    elif args.series.lower() == 'b':
                        instance.handleLTITestB()
                    else:
                        print("Invalid test series, try A or B.")
                else:
                    print("Syntax: python3 srtm_fw_control.py -m run <Test Unit> test <Series>")
            else:
                print("Syntax: python3 srtm_fw_control.py -m run LTI test <Series>")
    else:
        if args.sub is not None:
            print('Argument detected, but you did not enter a mode:\n')
            print("Syntax: python3 srtm_fw_control.py -m <Mode> <Group> <Reg>\n")
            print("Example: python3 srtm_fw_control.py -m write board axi_boardinfo_user_reg5")
        else:
            instance.run()

if __name__ == "__main__":
    main()