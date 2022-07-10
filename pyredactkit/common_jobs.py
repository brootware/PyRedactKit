""" Common jobs class implementation """
import os
import sys
import math
import json


from pyredactkit.identifiers import Identifier
id_object = Identifier()


class CommonJobs:
    """Common Jobs class
    Class containing all methods to support redaction
    of sensitive data

    Static variables:
        block (unicode string): To redact sensitive data
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

    def write_hashmap(self, hash_map: dict, filename: str, savedir="./") -> dict:
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

    def compute_total_words(self, filename: str) -> int:
        """Function to compute total words in a file.
        Args:
            filename (str): File to count the words

        Returns:
            total_words (int): total words in file
        """
        total_words = 0
        word_length = 5
        try:
            with open(filename, encoding="utf-8") as target_file:
                text_chunk = target_file.read()
                for current_text in text_chunk:
                    total_words += len(current_text)/word_length
        except UnicodeDecodeError:
            sys.exit("[-] Unable to read target file")
        return math.ceil(total_words)

    def compute_reading_minutes(self, total_words: int) -> int:
        # Words per minute
        WPM = 75
        return math.ceil(total_words/WPM)

    def compute_reading_hours(self, reading_minutes: int) -> int:
        return math.floor(reading_minutes/60)

    def process_report(self, filename: str):
        """Function to process calculate and generate report of man hour saved.
        Args:
            filename (str): File to count the words

        Returns:
            Creates a report on estimated man hours/minutes saved.
        """
        total_words = self.compute_total_words(filename)
        reading_minutes = self.compute_reading_minutes(total_words)
        reading_hours = self.compute_reading_hours(reading_minutes)

        word_report = f"[+] Estimated total words : {total_words}"
        minutes_saved = f"[+] Estimated total minutes saved : {reading_minutes}"
        man_hours_saved = f"[+] Estimated total man hours saved : {reading_hours}"

        print(word_report)
        print(minutes_saved)
        print(man_hours_saved)
