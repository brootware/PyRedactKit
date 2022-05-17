import re
import hashlib
import json
import os
import sys


def unredact(lookup_file, redacted_file):
    with open(redacted_file, encoding="utf-8") as redacted_target:
        try:
            with open(lookup_file, encoding="utf-8") as lookup_target:
                with open("unredacted_file.txt", "w", encoding="utf-8") as write_file:
                    content = json.load(lookup_target)
                    for key, value in content.items():
                        for line in redacted_target:
                            if key in line:
                                print(line)
                            # print(line)
                            # line = line.replace(key, value)
                            # write_file.write(line)
        except FileNotFoundError:
            sys.exit(f"[ - ] {lookup_file} file was not found")
        except json.JSONDecodeError:
            sys.exit(f"[ - ] Issue decoding {lookup_file} file")


unredact(".hashshadow.json", "redacted_test.txt")
