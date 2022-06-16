""" Main redactor class implementation """

import mimetypes
import os
import sys
import re
import math
import json
import uuid
import importlib

from pyredactkit.identifiers import Identifier
id_object = Identifier()
""" Main redactor library """


class Redactor:
    """Redactor class
    Class containing all methods to support redaction
    of sensitive data

    Static variables:
        block (unicode string): To redact sensitive data
    """

    block = "\u2588" * 15

    def __init__(self) -> None:
        """
        Class Initialization
        Args:
            None

        Returns:
            None
        """
        self.__allowed_files__ = [
            "text/plain",
            "text/x-python",
            "application/json",
            "application/javascript",
            "text/html",
            "text/csv",
            "text/tab-separated-values",
            "text/css",
            "text/cache-manifest",
            "text/calendar",
        ]

    @staticmethod
    def check_file_type(file):
        """Checks for the supplied file type
        Args:
            file (str): Filename of file to check
        Returns:
            mime (str): Mime type
        """
        if not os.path.isfile(file):
            return (None, None)
        return mimetypes.guess_type(file)[0]

    def get_allowed_files(self):
        """Gets a list of allowed files
        Args:
            None
        Returns:
            allowed_file (list): List of allowed files
        """
        return self.__allowed_files__

    def allowed_file(self, file):
        """Checks if supplied file is allowed
        Checks the supplied file to see if it is in the allowed_files list
        Args:
            file (str): File to check
        Returns:
            False: File not found / File type is not allowed
            True: File is allowed
        """
        if not os.path.isfile(file):
            return False
        return mimetypes.guess_type(file)[0] in self.get_allowed_files()

    def custom_patterns(self, custom_file):
        '''Load Rules
        Loads either a default ruleset or a self defined ruleset.
        Rules are loaded to patterns variable
        Args:
            custom_file (str): Custom rule file to be loaded
        Returns:
            json
        '''
        try:
            with open(custom_file, encoding="utf-8") as customfile:
                return json.load(customfile)
        except FileNotFoundError:
            sys.exit("[-] Pattern file was not found")
        except json.JSONDecodeError:
            sys.exit("[-] Issue decoding json file. This might be an error with your regex pattern.")

    def write_hashmap(self, hash_map=dict, filename=str, savedir="./") -> dict:
        """Function that writes a .hashshadow_file.txt.json to os directory.
        Args:
            hash_map (dictionary): dictionary object to be written to file.
            filename (str): name of supplied file

        Returns:
            Writes .hashshadow_file.txt.json to os directory
        """
        with open(f"{savedir}.hashshadow_{os.path.basename(filename)}.json", "w", encoding="utf-8") as file:
            json.dump(hash_map, file)

    def valid_options(self) -> tuple:
        """Function to read in valid options from Identifier.regexes
        Args:
            None

        Returns:
            option_tupe (tuple): redacted line
        """
        option_tuple = ()
        for id in id_object.regexes:
            option_tuple += id['type']
        return option_tuple

    def redact_custom(self, line=str, customfile=str) -> tuple:
        """Function to redact custom option
        Args:
            line (str) : line to be supplied to redact
            option (str): (optional) choice for redaction
            filename (str): name of supplied file

        Returns:
            line (str): redacted line
            kv_pair (dict) : key value pair of uuid to sensitive data.
        """
        custom_pattern = self.custom_patterns(customfile)
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

    def redact_all(self, line=str) -> tuple:
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

    def redact_name(self, data=str) -> tuple:
        """Main function to redact
        Args:
            data (str) : data to be supplied to identify names

        Returns:
            data (str) : redacted names from the data
            name_count (int) : number of names redacted from the data
        """
        name_list = id_object.names(data)
        name_count = len(name_list)
        for name in name_list:
            data = data.replace(name, self.block)
        return data, name_count

    def process_text(self, text=str, savedir="./"):
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
            self.write_hashmap(hash_map, generated_file, savedir)
            print(
                f"[+] .hashshadow_{os.path.basename(generated_file)}.json file generated. Keep this safe if you need to undo the redaction.")
            print(
                f"[+] Redacted and results saved to {os.path.basename(generated_file)}")

    def process_custom_file(self, filename, customfile=str, savedir="./"):
        """Function to process supplied file with custom regex file from cli.
        Args:
            filename (str): File to redact
            customfile (str): custom regex pattern for redaction
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
                        + " directory does not exist, creating it."
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
                    # The supplied custom regex pattern file will be used to redact the file
                    print(f"[+] {customfile} file supplied, will be redacting all supplied custom regex patterns")
                    hash_map = {}

                    for line in target_file:
                        # count elements to be redacted
                        for id in id_object.regexes:
                            if re.search(id['pattern'], line):
                                count += 1
                        # redact all and write hashshadow
                        data = self.redact_custom(line, customfile)
                        redacted_line = data[0]
                        kv_pairs = data[1]
                        hash_map.update(kv_pairs)
                        result.write(redacted_line)
                    self.write_hashmap(hash_map, filename, savedir)
                    print(
                        f"[+] .hashshadow_{os.path.basename(filename)}.json file generated. Keep this safe if you need to undo the redaction.")
                    print(f"[+] Redacted {count} targets...")
                    print(
                        f"[+] Redacted results saved to {savedir}redacted_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[-] Removed incomplete redact file")
            sys.exit("[-] Unable to read file")

    def process_core_file(self, filename, savedir="./"):
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
                        + " directory does not exist, creating it."
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
                    self.write_hashmap(hash_map, filename, savedir)
                    print(
                        f"[+] .hashshadow_{os.path.basename(filename)}.json file generated. Keep this safe if you need to undo the redaction.")
                    print(f"[+] Redacted {count} targets...")
                    print(
                        f"[+] Redacted results saved to {savedir}redacted_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[-] Removed incomplete redact file")
            sys.exit("[-] Unable to read file")

    def process_report(self, filename, savedir="./"):
        """Function to process calculate and generate report of man hour saved.
        Args:
            filename (str): File to count the words

        Returns:
            Creates a report on estimated man hours/minutes saved.
        """
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
                        + " directory does not exist, creating it."
                    )
                    os.makedirs(os.path.dirname(savedir))

                text_chunk = target_file.read()

                # Words per minute
                WPM = 75

                word_length = 5
                total_words = 0
                for current_text in text_chunk:
                    total_words += len(current_text)/word_length

                total_words = math.ceil(total_words)

                # Divide total words by words per minute read to get minutes and hour estimate.
                reading_minutes = math.ceil(total_words/WPM)
                reading_hours = math.floor(reading_minutes/60)

                word_report = f"[+] Estimated total words : {total_words}"
                minutes_saved = f"[+] Estimated total minutes saved : {reading_minutes}"
                man_hours_saved = f"[+] Estimated total man hours saved : {reading_hours}"

                print(word_report)
                print(minutes_saved)
                print(man_hours_saved)
                # Open a file write pointer as result
                # with open(
                #     f"{savedir}manhours_saved_{os.path.basename(filename)}",
                #     "w",
                #     encoding="utf-8",
                # ) as result:
                #     result.write(word_report + "\n" +
                #                  minutes_saved + "\n" + man_hours_saved)
                #     print(
                #         f"[+] Estimated man hours saved report saved to {savedir}manhours_saved_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"manhour_saved_report_{os.path.basename(filename)}")
            print("[-] Removed incomplete report")
            sys.exit("[-] Unable to read target file")
