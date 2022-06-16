#!/usr/bin/env python
"""
Utility to redact sensitive data
"""

import argparse

from pyredactkit.redact import Redactor
from pyredactkit.unredact import Unredactor
import os
import glob
import sys

# Creating instances of redact and unredact classes
redact_obj = Redactor()
unredact_obj = Unredactor()


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

help_menu = """
    PyRedactKit - Redact and Un-redact any sensitive data from your text files!

    Github:\n
    https://github.com/brootware/pyredactkit
    
    Follow me on Twitter!\n
    https://twitter.com/brootware
    
    Example usage:\n
        pyredactkit --text 'This is my ip: 127.0.0.1. My email is brute@gmail.com'\n
        pyredactkit --file [file/filestoredact]\n
        pyredactkit --file redacted_file --unredact .hashshadow.json\n
        pyredactkit --file file --customfile custom.json\n
    """


def arg_helper() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Supply a sentence or paragraph to redact sensitive data from it. Or read in a file or set of files with -f to redact",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "text",
        type=str,
        help="""Redact sensitive data of a sentence from command prompt.""",
        nargs="*"
    )
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    parser.add_argument(
        "-f",
        "--file",
        nargs="+",
        help="""Path of a file or a directory of files."""
    )
    parser.add_argument(
        "-u",
        "--unredact",
        help="""
                Option to unredact masked data.
                Usage: pyredactkit -f [redacted_file] -u [.hashshadow.json]
                """
    )
    parser.add_argument(
        "-d",
        "--dirout",
        help="""
                Output directory of the file.
                Usage: pyredactkit -f [file/filestoredact] -d [redacted_dir]
                """
    )
    parser.add_argument(
        "-c",
        "--customfile",
        help="""
                User defined custom regex pattern for redaction.
                Usage: pyredactkit -f [file/filestoredact] -c [customfile.json]
                """
    )
    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        default=True,
        help='Search through subfolders'
    )
    parser.add_argument(
        '-e',
        '--extension',
        default='',
        help='File extension to filter by.'
    )
    args = parser.parse_args()

    return args


def execute_file_arg() -> None:
    args = arg_helper()
    full_paths = [os.path.join(os.getcwd(), path) for path in args.file]
    files = set()

    for path in full_paths:
        if os.path.isfile(path):
            file_name, file_ext = os.path.splitext(path)
            if args.extension in ('', file_ext):
                files.add(path)
        elif args.recursive:
            full_paths += glob.glob(path + '/*')

    for file in files:
        if args.customfile:
            redact_obj.process_custom_file(file, args.customfile)
            redact_obj.process_report(file)
        elif args.dirout:
            redact_obj.process_core_file(file, args.dirout)
            redact_obj.process_custom_file(file, args.custom, args.dirout)
            redact_obj.process_report(file, args.dirout)
        elif args.unredact:
            unredact_obj.unredact(file, args.unredact)
        else:
            redact_obj.process_core_file(file)
            redact_obj.process_report(file)


def main():
    print(banner)

    args = arg_helper()
    if args.file or (args.file and args.dirout):
        execute_file_arg()
    else:
        redact_obj.process_text(args.text)


if __name__ == "__main__":
    main()
