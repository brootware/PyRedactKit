#!/usr/bin/env python
"""
Utility to redact sensitive data
"""

from pyredactkit.core_redactor import CoreRedactorEngine
from pyredactkit.custom_redactor import CustomRedactorEngine
from pyredactkit.unredact import Unredactor
import argparse
import os
import glob
import sys

# Creating instances of redact and unredact classes
core_redact = CoreRedactorEngine()
custom_redact = CustomRedactorEngine()
unredact_obj = Unredactor()


banner = r"""
__________         __________           .___              __     ____  __.__  __   
\______   \___.__. \______   \ ____   __| _/____    _____/  |_  |    |/ _|__|/  |_ 
 |     ___<   |  |  |       _// __ \ / __ |\__  \ _/ ___\   __\ |      < |  \   __\
 |    |    \___  |  |    |   \  ___// /_/ | / __ \\  \___|  |   |    |  \|  ||  |  
 |____|    / ____|  |____|_  /\___  >____ |(____  /\___  >__|   |____|__ \__||__|  
           \/              \/     \/     \/     \/     \/               \/                                                                                                                 
                    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
                    |P|o|w|e|r|e|d| |b|y| |B|r|o|o|t|w|a|r|e|
                    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
            
    https://github.com/brootware
    https://brootware.github.io     
    https://twitter.com/brootware                                                                        
    """

help_menu = """
    PyRedactKit - Redact and Un-redact any sensitive data from your text files!
    Example usage:\n
        prk 'This is my ip: 127.0.0.1. My email is brute@gmail.com. My favorite secret link is github.com'\n
        prk [file/directory_with_files]\n
        prk redacted_file --unredact .hashshadow.json\n
        prk file --customfile custom.json\n
    """


def arg_helper() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Supply either a text chunk or file name path to redact sensitive data from it.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "text",
        help="""Supply either a text chunk or file name path to redact sensitive data from command prompt.""",
        nargs="*"
    )
    if len(sys.argv) == 1:
        print(help_menu)
        parser.print_help(sys.stderr)
        sys.exit(1)
    parser.add_argument(
        "-u",
        "--unredact",
        help="""
                Option to unredact masked data.
                Usage: pyredactkit [redacted_file] -u [.hashshadow.json]
                """
    )
    parser.add_argument(
        "-d",
        "--dirout",
        help="""
                Output directory of the file.
                Usage: pyredactkit [file/filestoredact] -d [redacted_dir]
                """
    )
    parser.add_argument(
        "-c",
        "--customfile",
        help="""
                User defined custom regex pattern for redaction.
                Usage: pyredactkit [file/filestoredact] -c [customfile.json]
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


def is_it_file(file_path: str) -> bool:
    return os.path.isfile(file_path) or os.path.isdir(file_path)


def recursive_file_search(full_path: str, extension: str, recursive: bool) -> set:
    full_paths = [os.path.join(os.getcwd(), path) for path in full_path]
    files = set()
    for path in full_paths:
        if os.path.isfile(path):
            file_name, file_ext = os.path.splitext(path)
            if extension in ('', file_ext):
                files.add(path)
        elif recursive:
            full_paths += glob.glob(path + '/*')
    return files


def execute_redact_logic() -> None:
    args = arg_helper()

    is_text = is_it_file(args.text[0])
    if not is_text:
        core_redact.process_text(args.text)

    files = recursive_file_search(args.text, args.extension, args.recursive)

    for file in files:
        if args.customfile and args.dirout:
            custom_redact.process_custom_file(file, args.customfile, args.dirout)
        elif args.customfile:
            custom_redact.process_custom_file(file, args.customfile)
        elif args.dirout:
            core_redact.process_core_file(file, args.dirout)
        elif args.unredact:
            unredact_obj.unredact(file, args.unredact)
        else:
            core_redact.process_core_file(file)


def main():
    print(banner)
    execute_redact_logic()


def api_identify_sensitive_data(text: str) -> list:
    return core_redact.identify_data(text)


if __name__ == "__main__":
    main()
