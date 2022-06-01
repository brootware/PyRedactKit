""" Main redactor class implementation """

import mimetypes
import os
import sys
import re
import math
import json
import uuid

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

    def __init__(self):
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

    def write_hashmap(self, hash_map=dict, filename=str):
        """Function that writes a .hashshadow_file.txt.json to os directory.
        Args:
            hash_map (dictionary): dictionary object to be written to file.
            filename (str): name of supplied file

        Returns:
            Writes .hashshadow_file.txt.json to os directory
        """
        with open(f".hashshadow_{os.path.basename(filename)}.json", "w", encoding="utf-8") as file:
            json.dump(hash_map, file)

    def valid_options(self):
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

    def redact_specific(self, line=str, option=str, filename=str):
        """Function to redact specific option
        Args:
            line (str) : line to be supplied to redact
            option (str): (optional) choice for redaction
            filename (str): name of supplied file

        Returns:
            line (str): redacted line
        """
        hash_map = {}

        for id in id_object.regexes:
            redact_pattern = id['pattern']
            if option in id['type'] and re.search(
                    redact_pattern, line, flags=re.IGNORECASE):
                pattern_string = re.search(
                    redact_pattern, line, flags=re.IGNORECASE)
                pattern_string = pattern_string.group(0)
                masked_data = str(uuid.uuid4())
                hash_map.update({masked_data: pattern_string})
                line = re.sub(
                    redact_pattern, masked_data, line, flags=re.IGNORECASE)

        self.write_hashmap(hash_map, filename)
        return line

    def redact_name(self, data=str):
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

    def process_file(self, filename, option=str, savedir="./"):
        """Function to process supplied file from cli.
        Args:
            filename (str): File to redact
            savedir (str): [Optional] directory to place results

        Returns:
            Creates redacted file.
        """
        count = 0
        hash_map = {}
        options_list = self.valid_options()
        try:
            # Open a file read pointer as target_file
            with open(filename, encoding="utf-8") as target_file:
                if savedir != "./" and savedir[-1] != "/":
                    savedir = savedir + "/"

                # created the directory if not present
                if not os.path.exists(os.path.dirname(savedir)):
                    print(
                        "[ + ] "
                        + os.path.dirname(savedir)
                        + " directory does not exist, creating it."
                    )
                    os.makedirs(os.path.dirname(savedir))

                print(
                    "[ + ] Processing starts now. This may take some time "
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
                    if type(option) is not str:
                        print(
                            f"[ + ] No option supplied, will be redacting all the sensitive data supported")
                        for line in target_file:
                            for p in id_object.regexes:
                                redact_pattern = p['pattern']
                                if re.search(redact_pattern, line, flags=re.IGNORECASE):
                                    count += 1
                                    pattern_string = re.search(
                                        redact_pattern, line, flags=re.IGNORECASE)
                                    pattern_string = pattern_string.group(0)
                                    masked_data = str(uuid.uuid4())
                                    hash_map.update(
                                        {masked_data: pattern_string})
                                    line = re.sub(redact_pattern, masked_data, line,
                                                  flags=re.IGNORECASE)
                            result.write(line)
                        self.write_hashmap(hash_map, filename)
                        print(
                            f"[ + ].hashshadow_{os.path.basename(filename)}.json file generated. Keep this safe if you need to undo the redaction.")
                    # Separate option to redact names
                    elif option in ("name", "names"):
                        content = target_file.read()
                        data = self.redact_name(content)
                        result.write(data[0])
                        count = data[1]
                    elif option not in options_list:
                        os.remove(
                            f"{savedir}redacted_{os.path.basename(filename)}")
                        sys.exit(
                            "[ - ] Not a valid option for redaction type.")
                    # Redacts all other options here
                    else:
                        print(f"[ + ] Redacting {option} from the file")
                        for line in target_file:
                            for id in id_object.regexes:
                                if option in id['type'] and re.search(id['pattern'], line, flags=re.IGNORECASE):
                                    count += 1
                            line = self.redact_specific(line, option, filename)
                            result.write(line)
                        print(
                            f"[ + ].hashshadow_{os.path.basename(filename)}.json file generated. Keep this safe if you need to undo the redaction.")

                    print(f"[ + ] Redacted {count} targets...")
                    print(
                        f"[ + ] Redacted results saved to {savedir}redacted_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[ - ] Removed incomplete redact file")
            sys.exit("[ - ] Unable to read file")

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
                        "[ + ] "
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

                word_report = f"[ + ] Estimated total words : {total_words}"
                minutes_saved = f"[ + ] Estimated total minutes saved : {reading_minutes}"
                man_hours_saved = f"[ + ] Estimated total man hours saved : {reading_hours}"

                # Open a file write pointer as result
                with open(
                    f"{savedir}manhours_saved_{os.path.basename(filename)}",
                    "w",
                    encoding="utf-8",
                ) as result:
                    result.write(word_report + "\n" +
                                 minutes_saved + "\n" + man_hours_saved)
                    print(
                        f"[ + ] Estimated man hours saved report saved to {savedir}manhours_saved_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"manhour_saved_report_{os.path.basename(filename)}")
            print("[ - ] Removed incomplete report")
            sys.exit("[ - ] Unable to read target file")
