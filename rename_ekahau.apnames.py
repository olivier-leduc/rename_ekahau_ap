#!/usr/local/bin/python3
# rename_ekahau_apnames.py
#
__author__  = "Olivier Le Duc"
__version__ = "0.1"

""" This script renames default Ekahau AP names into your own AP names, given a textfile containing a list of AP names to BSSIDs.
    The *esx file is essentially a zip file that contains all the survey data (measurements, images, metadata).
    This script will update entries in the accessPoints.json file and renames generically named APs ("Measured AP-XX:XX" into
    AP names of your liking. The esx file needs to be unzipped prior to executing this script.

"""

import json, os, sys
import argparse

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def initialize():
    # Change to a generally reliable working directory.
    os.chdir(os.environ['HOME'])

    parser = argparse.ArgumentParser(description='some information',
        usage='use "python %(prog)s --help" for more information',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-b", dest="bssidmapping", required=True,
                        help="Input the full path of the file containing AP<->BSSID mapping.\nex: /Users/johnsmith/bssidmap.csv\nThe file should be using this format:\nap1,f0:72:ea:18:37:cd\nap2,f0:9f:c2:a4:67:e8", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-f", dest="esxfolder", required=True,
                        help="Input the full path of the UNZIPPED esx file.\nex: /Users/johnsmith/warehousesurvey/", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    return parser


def main():
    with open(args.bssidmapping) as f:
      bssidmapping_list = f.readlines()
      bssidmapping = {}
      for line in bssidmapping_list:
        # TODO: add exception for misformatted lines.
        row = line.strip().split(',')
        bssidmapping[row[0]] = row[1].lower()

    with open(os.path.join(args.esxfolder, 'accessPoints.json')) as f:
      esxdata = json.load(f)

    for apname, bssid in bssidmapping.items():
      for ap in esxdata['accessPoints']:
        # TODO: add exception for repeated last 4 octets (it might happen).
        if bssid[-5:] in ap['name'] :
          ap['name'] = ap['name'].replace(ap['name'], apname)


    with open(os.path.join(args.esxfolder, 'accessPoints.json'), 'w') as f:
      json.dump(esxdata, f, indent=4)

if __name__ == '__main__':
    parser = initialize()
    args = parser.parse_args()
    main()

