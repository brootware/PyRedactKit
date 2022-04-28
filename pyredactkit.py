#!/usr/bin/env python
"""
Utility to redact sensitive data
"""

import argparse
from src.redact import Redactor
import os
import glob
# lintertest

banner = """
    ______       ______         _            _     _   ___ _   
    | ___ \      | ___ \       | |          | |   | | / (_) |  
    | |_/ /   _  | |_/ /___  __| | __ _  ___| |_  | |/ / _| |_ 
    |  __/ | | | |    // _ \/ _` |/ _` |/ __| __| |    \| | __|
    | |  | |_| | | |\ \  __/ (_| | (_| | (__| |_  | |\  \ | |_ 
    \_|   \__, | \_| \_\___|\__,_|\__,_|\___|\__| \_| \_/_|\__|
           __/ |                                               
           |___/                                                                                                           
            +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
            |P|o|w|e|r|e|d| |b|y| |B|r|o|o|t|w|a|r|e|
            +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
            
    https://github.com/brootware
    https://brootware.github.io                                                                             
    """


def main():
    print(banner)

    parser = argparse.ArgumentParser(description='Read in a file or set of files, and return the result.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("path", nargs="+",
                        help="Path of a file or a directory of files")
    parser.add_argument(
        "-t", "--redactiontype", help="""Type of data to redact. 
        names,
        nric,
        dns,
        emails,
        ipv4,
        ipv6""")
    parser.add_argument(
        "-d", "--dirout", help="Output directory of the file")
    parser.add_argument('-r', '--recursive', action='store_true',
                        default=True, help='Search through subfolders')
    parser.add_argument('-e', '--extension', default='',
                        help='File extension to filter by.')
    args = parser.parse_args()

    full_paths = [os.path.join(os.getcwd(), path) for path in args.path]
    files = set()

    for path in full_paths:
        if os.path.isfile(path):
            file_name, file_ext = os.path.splitext(path)
            if args.extension in ('', file_ext):
                files.add(path)
        elif args.recursive:
            full_paths += glob.glob(path + '/*')

    # redact file
    redact_obj = Redactor()

    for file in files:
        if args.redactiontype:
            redact_obj.process_file(file, args.redactiontype)
        elif args.dirout:
            redact_obj.process_file(file, args.redactiontype, args.dirout)
        else:
            redact_obj.process_file(file)


if __name__ == "__main__":
    main()
