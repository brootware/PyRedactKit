""" Custom redactor engine class implementation """
import os
import sys
import re
import json
import uuid
from pyredactkit.common_jobs import CommonJobs
cj_object = CommonJobs()


class CustomRedactorEngine:
    """CustomRedactorEngine class
    Class containing all methods to support redaction
    of custom sensitive data type defined by user

    Static variables:
        None
    """
    dir_create = " directory does not exist, creating it."

    def __init__(self) -> None:
        """
        Class Initialization
        Args:
            None

        Returns:
            None
        """
        return None

    def read_custom_patterns(self, custom_file: str) -> list:
        '''Load Rules
        Loads either a default ruleset or a self defined ruleset.
        Rules are loaded to patterns variable
        Args:
            custom_file (str): Custom rule file to be loaded
        Returns:
            patterns (list): list of custom patterns
        '''
        try:
            with open(custom_file, encoding="utf-8") as customfile:
                return json.load(customfile)
        except FileNotFoundError:
            sys.exit("[-] Pattern file was not found")
        except json.JSONDecodeError:
            sys.exit("[-] Issue decoding json file. This might be an error with your regex pattern.")

    def redact_custom(self, line: str, customfile: str) -> tuple:
        """Function to redact custom option
        Args:
            line (str) : line to be supplied to redact
            customfile (str): (optional) choice for redaction

        Returns:
            line (str): redacted line
            kv_pair (dict) : key value pair of uuid to sensitive data.
        """
        custom_pattern = self.read_custom_patterns(customfile)
        kv_pairs = {}
        for id in range(len(custom_pattern)):
            redact_pattern = custom_pattern[id]['pattern']
            if re.search(redact_pattern, line, re.IGNORECASE):
                pattern_string = re.search(redact_pattern, line)
                pattern_string = pattern_string.group(0)
                masked_data = str(uuid.uuid4())
                kv_pairs.update({masked_data: pattern_string})
                line = re.sub(redact_pattern, masked_data, line)
        return line, kv_pairs

    def process_custom_file(self, file_name: str, customfile: str, make_dir="./"):
        """Function to process supplied file with custom regex file from cli.
        Args:
            file_name (str): File to redact
            customfile (str): custom regex pattern for redaction
            make_dir (str): [Optional] directory to place results

        Returns:
            Creates redacted file.
        """
        redact_count = 0
        secret_map = {}
        try:
            # Open a file read pointer as target_file
            with open(file_name, encoding="utf-8") as target_file:
                if make_dir != "./" and make_dir[-1] != "/":
                    make_dir = make_dir + "/"

                # created the directory if not present
                if not os.path.exists(os.path.dirname(make_dir)):
                    print(
                        "[+] "
                        + os.path.dirname(make_dir)
                        + f"{self.dir_create}"
                    )
                    os.makedirs(os.path.dirname(make_dir))

                print(
                    "[+] Processing starts now. This may take some time "
                    "depending on the file size. Monitor the redacted file "
                    "size to monitor progress"
                )

                # Open a file write pointer as result
                with open(
                    f"{make_dir}redacted_{os.path.basename(file_name)}",
                    "w",
                    encoding="utf-8",
                ) as result:
                    # The supplied custom regex pattern file will be used to redact the file
                    print(f"[+] {customfile} file supplied, will be redacting all supplied custom regex patterns")
                    secret_map = {}
                    custom_pattern = self.read_custom_patterns(customfile)
                    for line in target_file:
                        # redact_count elements to be redacted
                        for id in range(len(custom_pattern)):
                            if re.search(custom_pattern[id]['pattern'], line):
                                redact_count += 1
                        # redact all and write hashshadow
                        data = self.redact_custom(line, customfile)
                        redacted_line = data[0]
                        kv_pairs = data[1]
                        secret_map.update(kv_pairs)
                        result.write(redacted_line)
                    cj_object.write_hashmap(secret_map, file_name, make_dir)
                    print(
                        f"[+] .hashshadow_{os.path.basename(file_name)}.json file generated. Keep this safe if you need to undo the redaction.")
                    print(f"[+] Redacted {redact_count} targets...")
                    print(
                        f"[+] Redacted results saved to {make_dir}redacted_{os.path.basename(file_name)}")
                    cj_object.process_report(file_name)

        except UnicodeDecodeError:
            os.remove(f"{make_dir}redacted_{os.path.basename(file_name)}")
            print("[-] Removed incomplete redact file")
            sys.exit("[-] Unable to read file")
