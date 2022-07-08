import json
import sys
import os


class Unredactor:
    """Redactor class
    Class containing all methods to support un-redaction
    of masked data

    """

    def __init__(self) -> None:
        """
        Class Initialization
        Args:
            None

        Returns:
            None
        """

    def replace_all(self, text: str, dictionary: dict) -> str:
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

    def unredact(self, redacted_file: str, lookup_file: str) -> None:
        """Function to unredact masked data and produces original unredacted data.
        Args:
            redacted_file (str): Name of the redacted file
            lookup_file (str): Name of the file to look up key value map of masked data and original data.


        Returns:
            Writes unredacted_file.txt with original unmasked data.
        """
        with open(redacted_file, encoding="utf-8") as redacted_target:
            try:
                with open(lookup_file, encoding="utf-8") as lookup_target:
                    content = json.load(lookup_target)
                    with open(f"unredacted_{os.path.basename(redacted_file)}", "w", encoding="utf-8") as write_file:
                        print("[+] Unredaction started. This will take some time.")
                        for line in redacted_target:
                            line = self.replace_all(line, content)
                            write_file.write(line)
                        print(
                            f"[+] Unredacted results saved to unredacted_{os.path.basename(redacted_file)}")
            except FileNotFoundError:
                sys.exit(f"[-] {lookup_file} file was not found")
            except json.JSONDecodeError:
                sys.exit(f"[-] Issue decoding {lookup_file} file")
