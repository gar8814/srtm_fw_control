from FirmwareControl import FirmwareControl
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', default=False, help='Use fake ipbus')
    args = parser.parse_args()
    instance = FirmwareControl(args.debug)
    instance.run()

if __name__ == "__main__":
    main()