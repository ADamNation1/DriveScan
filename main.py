
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
    parser.add_argument('-o', '--output', metavar='out', type=str, required=True, help='one output directory')

    args = parser.parse_args()
    output_location = args.output

    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        logging.info("Verbose output enabled")

    if not output_location.endswith('\\'):
        output_location += "\\"

    for i, directory in enumerate(args.directories):
        logging.info("Creating Output file: " + output_location + "Directory" + str(i) + ".txt")
        with open(output_location + "Directory" + str(i) + ".txt", "w") as f:
            logging.info("Walking...")
            for dirName, subdirList, fileList in os.walk(directory):
                logging.info('Directory: %s\n' % dirName)
                f.write(dirName + "\n")
                for fileName in fileList:
                    logging.info('\t%s' % fileName)
                    f.write("\t" + fileName + "\n")
                f.write("\n")
main()

