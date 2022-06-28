""" Core redactor engine class implementation """
from pyredactkit.common_jobs import CommonJobs
from pyredactkit.identifiers import Identifier
import os
import sys
import re
import uuid

# Instantiate identifier and commonjobs objects
id_object = Identifier()
cj_object = CommonJobs()
""" Coreredactor library """


class CoreRedactorEngine:
    """CoreRedactorEngine class
    Class containing all methods to support redaction
    of core sensitive data type

    Static variables:
        block (unicode string): To redact sensitive data
    """

    block = "\u2588" * 15
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

    def redact_all(self, line: str) -> tuple:
        """Function to redact specific option
        Args:
            line (str) : line to be supplied to redact

        Returns:
            line (str): redacted line
            kv_pair (dict) : key value pair of uuid to sensitive data.
        """
        hash_map = {}
        for id in id_object.regexes:
            redact_pattern = id['pattern']
            if re.search(redact_pattern, line):
                pattern_string = re.search(redact_pattern, line)
                pattern_string = pattern_string.group(0)
                masked_data = str(uuid.uuid4())
                hash_map.update({masked_data: pattern_string})
                line = re.sub(redact_pattern, masked_data, line)
        return line, hash_map

    def process_text(self, text: str, savedir="./"):
        """Function to process supplied text from cli.
        Args:
            text (str): string to redact
            savedir (str): [Optional] directory to place results

        Returns:
            Creates redacted file.
        """
        hash_map = {}
        generated_file = f"redacted_file_{str(uuid.uuid1())}.txt"
        with open(
            f"{generated_file}",
            "w",
            encoding="utf-8",
        ) as result:
            for line in text:
                data = self.redact_all(line)
                redacted_line = data[0]
                kv_pairs = data[1]
                hash_map.update(kv_pairs)
                result.write(f"{redacted_line}\n")
            cj_object.write_hashmap(hash_map, generated_file, savedir)
            print(
                f"[+] .hashshadow_{os.path.basename(generated_file)}.json file generated. Keep this safe if you need to undo the redaction.")
            print(
                f"[+] Redacted and results saved to {os.path.basename(generated_file)}")

    def process_core_file(self, filename: str, savedir="./"):
        """Function to process supplied file from cli.
        Args:
            filename (str): File to redact
            savedir (str): [Optional] directory to place results

        Returns:
            Creates redacted file.
        """
        count = 0
        hash_map = {}
        try:
            # Open a file read pointer as target_file
            with open(filename, encoding="utf-8") as target_file:
                if savedir != "./" and savedir[-1] != "/":
                    savedir = savedir + "/"

                # created the directory if not present
                if not os.path.exists(os.path.dirname(savedir)):
                    print(
                        "[+] "
                        + os.path.dirname(savedir)
                        + f"{self.dir_create}"
                    )
                    os.makedirs(os.path.dirname(savedir))

                print(
                    "[+] Processing starts now. This may take some time "
                    "depending on the file size. Monitor the redacted file "
                    "size to monitor progress"
                )

                # Open a file write pointer as result
                with open(
                    f"{savedir}redacted_{os.path.basename(filename)}",
                    "w",
                    encoding="utf-8",
                ) as result:
                    # Check if any redaction type option is given in argument. If none, will redact all sensitive data.
                    print("[+] No custom regex pattern supplied, will be redacting all the core sensitive data supported")
                    hash_map = {}
                    for line in target_file:
                        # count elements to be redacted
                        for id in id_object.regexes:
                            if re.search(id['pattern'], line):
                                count += 1
                        # redact all and write hashshadow
                        data = self.redact_all(line)
                        redacted_line = data[0]
                        kv_pairs = data[1]
                        hash_map.update(kv_pairs)
                        result.write(redacted_line)
                    cj_object.write_hashmap(hash_map, filename, savedir)
                    print(
                        f"[+] .hashshadow_{os.path.basename(filename)}.json file generated. Keep this safe if you need to undo the redaction.")
                    print(f"[+] Redacted {count} targets...")
                    print(
                        f"[+] Redacted results saved to {savedir}redacted_{os.path.basename(filename)}")
                    cj_object.process_report(filename)

        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[-] Removed incomplete redact file")
            sys.exit("[-] Unable to read file")
