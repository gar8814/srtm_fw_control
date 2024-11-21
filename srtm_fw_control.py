from FirmwareControl import FirmwareControl
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', default=False, help='Use fake ipbus')
    parser.add_argument('-rb', '--readBoard', defualt=False, help='Read all registers')
    parser.add_argument('-lti', defualt=False, help='Go straight to LTI')
    args = parser.parse_args()
    instance = FirmwareControl(args.readBoard, args.debug)
    instance.run()

if __name__ == "__main__":
    main()
