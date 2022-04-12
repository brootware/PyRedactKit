#!/usr/bin/env python
"""
Utility to redact sensitive data
"""

import argparse
from src.redact import Redactor
import os
import sys


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Logfile to redact")
    parser.add_argument(
        "-t", "--redactiontype", help="""Type of data to redact. 
        names,
        dates,
        phones,
        dns,
        emails,
        ipv4,
        ipv6,
        cc(creditcard)""")
    parser.add_argument(
        "-o", "--outdir", help="Output directory of the file")
    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        sys.exit(f"[ - ] {args.filename} not present")

    # redact file
    redact_obj = Redactor

    if args.redactiontype and args.outdir:
        redact_obj.process_file(args.filename, args.redactiontype, args.outdir)
    elif args.redactiontype:
        redact_obj.process_file(args.filename, args.redactiontype)
    else:
        redact_obj.process_file(args.filename)


if __name__ == "__main__":
    main()
