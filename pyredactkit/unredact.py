import json
import sys


class Unredactor:
    """Redactor class
    Class containing all methods to support un-redaction
    of masked data

    """

    def __init__(self):
        """
        Class Initialization
        Args:
            None

        Returns:
            None
        """

    def replace_all(self, text, dictionary):
        """Function to replace all the text from string
        Args:
            text (str): A line of text in string format
            dictionary (dict): A key value pair of masked data and original data

        Returns:
            text (str): A line of text after replacing masked data with original data
        """
        for k, v in dictionary.items():
            text = text.replace(k, v)
        return text

    def unredact(self, lookup_file, redacted_file):
        """Function to unredact masked data and produces original unredacted data.
        Args:
            lookup_file (str): Name of the file to look up key value map of masked data and original data.
            redacted_file (str): Name of the redacted file

        Returns:
            Writes unredacted_file.txt with original unmasked data.
        """
        with open(redacted_file, encoding="utf-8") as redacted_target:
            try:
                with open(lookup_file, encoding="utf-8") as lookup_target:
                    with open(f"unredacted_{redacted_file}", "w", encoding="utf-8") as write_file:
                        content = json.load(lookup_target)
                        for line in redacted_target:
                            line = self.replace_all(line, content)
                            write_file.write(line)
            except FileNotFoundError:
                sys.exit(f"[ - ] {lookup_file} file was not found")
            except json.JSONDecodeError:
                sys.exit(f"[ - ] Issue decoding {lookup_file} file")
