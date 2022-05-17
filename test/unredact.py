import re
import hashlib
import json
import os
import sys
import fileinput


def unredact(redacted_file, lookup_file):
    with open(redacted_file, encoding="utf-8") as redacted_target:
        try:
            with open(lookup_file, encoding="utf-8") as lookup_target:
                content = json.load(lookup_target)
                with open("unredacted_file.txt", "w", encoding="utf-8") as write_file:
                    for line in redacted_target:
                        line = replace_all(line, content)
                        write_file.write(line)
        except FileNotFoundError:
            sys.exit(f"[ - ] {lookup_file} file was not found")
        except json.JSONDecodeError:
            sys.exit(f"[ - ] Issue decoding {lookup_file} file")


def replace_all(text, dictionary):
    for k, v in dictionary.items():
        text = text.replace(k, v)
    return text


unredact("redacted_test.txt", ".hashshadow.json")


# with fileinput.FileInput("redacted_test.txt", inplace=True, backup='.bak') as file:
#     for line in file:
#         line.replace("c9b72036-172d-461a-ab87-b1098ad5649d",
#                      "www.linkedin.com")

#     file.write(line)
