""" Common jobs class implementation """
import mimetypes
import os
import sys
import re
import math
import json
import uuid


class CommonJobs:
    """Common Jobs class
    Class containing all methods to support redaction
    of sensitive data

    Static variables:
        block (unicode string): To redact sensitive data
    """

    def __init__(self) -> None:
        """
        Class Initialization
        Args:
            None

        Returns:
            None
        """
        return None

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
                        + f"{self.dir_create}"
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
