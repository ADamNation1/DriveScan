
#!/usr/bin/python36
import argparse
import sys
import logging
import os

def list_dir(directory):
    logging.debug("Listing directory " + directory)

def main():
    parser = argparse.ArgumentParser(description='py directory scanner')
    parser.add_argument('-v', '--verbose', help='enable verbose output', action="store_true")
    parser.add_argument('-d', '--directories', metavar='dir', type=str, nargs='+', required=True, help='one or multiple directories')
    parser.add_argument('-o', '--output', metavar='dir', type=str, required=True, help='one output directory')

    args = parser.parse_args()
    output_location = args.output

    if str(output_location).endswith("\\"):
        output_location.append("\\")

    if(args.verbose):
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        logging.info("Verbose output enabled")

    for directory in args.directories:
        logging.info("Creating Output file: " + output_location + "directory1.txt")
        with open(output_location + "woof.txt", "w") as f:
            for root, dirs, files in os.walk(directory, topdown=True):
                for name in files:
                    print(os.path.join(root, name))
                    f.write(os.path.join(root, name))
                for name in dirs:
                    print(os.path.join(root, name))
                    f.write((os.path.join(root, name)))



main()

