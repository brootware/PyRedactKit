""" Main redactor class implementation """

import mimetypes
import os
import sys
import time
import re

from src.identifiers import Identifier

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

    # def to_redact(self, data=str, redact_list=[]):
    #     """Helper function that takes in list of keywords to be redacted from data.
    #     Args:
    #         redact_list (array): list of keywords in alpha-numeric format
    #         data (str): data to be redacted in alpha-numeric format

    #     Returns:
    #         data (str): redacted data
    #     """
    #     redact_count = 0
        

    #     for elm in redact_list:
    #         # multiply the block with 15 regardless of length
    #         bl = self.block * 15
    #         # substitute the block using regular expression
    #         data = data.replace(elm,bl)
    #         redact_count += 1

        
    #     print()
    #     print(f"[ + ] Redacted {redact_count} targets...")
    #     return data

    # def redact(self, data=str, option=str):
    #     """Main function to redact
    #     Args:
    #         data (str) : data to be supplied to redact
    #         option (str): (optional) choice for redaction

    #     Returns:
    #         redacted_data (str): redacted data
    #     """
    #     start = time.time()
    #     if option == "dns":
    #         print(
    #             f"[ + ] Redacting {option} from the file. This might take some time")
    #         dns_list = id_object.dns_strings(data)
    #         redacted_data = self.to_redact(data, dns_list)
    #     elif option in ("email", "emails"):
    #         print(
    #             f"[ + ] Redacting {option} from the file. This might take some time")
    #         emails_list = id_object.emails(data)
    #         redacted_data = self.to_redact(data, emails_list)
    #     elif option == "ipv4":
    #         print(
    #             f"[ + ] Redacting {option} from the file. This might take some time")
    #         ipv4_list = id_object.ipv4_addresses(data)
    #         redacted_data = self.to_redact(data, ipv4_list)
    #     elif option == "ipv6":
    #         print(
    #             f"[ + ] Redacting {option} from the file. This might take some time")
    #         ipv6_list = id_object.ipv6_addresses(data)
    #         redacted_data = self.to_redact(data, ipv6_list)
    #     elif option == "names":
    #         print(
    #             f"[ + ] Redacting {option} from the file. This might take some time")
    #         name_list = id_object.names(data)
    #         redacted_data = self.to_redact(data, name_list)
    #     elif option == "cc":
    #         print(
    #             f"[ + ] Redacting {option} from the file. This might take some time")
    #         cc_list = id_object.credit_cards(data)
    #         redacted_data = self.to_redact(data, cc_list)
    #     elif option == "nric":
    #         print(f"[ + ] Redacting {option} from the file. This might take some time")
    #         nric_list = id_object.nric(data)
    #         redacted_data = self.to_redact(data,nric_list)
    #     else:
    #         print(
    #             "[ + ] No option supplied, will be redacting all the sensitive data supported"
    #         )
    #         all_sensi = (
    #             id_object.emails(data)
    #             + id_object.dns_strings(data)
    #             + id_object.ipv4_addresses(data)
    #             + id_object.ipv6_addresses(data)
    #             + id_object.names(data)
    #             + id_object.credit_cards(data)
    #             + id_object.nric(data)
    #         )
    #         redacted_data = self.to_redact(data, all_sensi)
    #     end = time.time()
    #     time_taken = end - start
    #     print(f"[ + ] Took {time_taken} seconds to execute")
    #     return redacted_data
        
    def redact(self, line=str, option=str):
        redacted_line = ''
        if option == "dns":
            dns = id_object.regexes[1]['pattern']
            redacted_line = re.sub(dns, self.block, line,flags=re.IGNORECASE)
        elif option in ("email", "emails"):
            email = id_object.regexes[0]['pattern']
            redacted_line = re.sub(email, self.block, line,flags=re.IGNORECASE)
        elif option == "ipv4":
            ipv4 = id_object.regexes[2]['pattern']
            redacted_line = re.sub(ipv4, self.block, line,flags=re.IGNORECASE)
        # elif option == "names":
        #     print(
        #         f"[ + ] Redacting {option} from the file. This might take some time")
        #     name_list = id_object.names(data)
        #     redacted_line = self.to_redact(data, name_list)
        elif option in ("cc","creditcard"):
            cc = id_object.regexes[3]['pattern']
            redacted_line = re.sub(cc, self.block, line,flags=re.IGNORECASE)
        elif option in ("nric","fin"):
            nric = id_object.regexes[4]['pattern']
            redacted_line = re.sub(nric, self.block, line,flags=re.IGNORECASE)
        elif option == "ipv6":
            ipv6 = id_object.regexes[5]['pattern']
            redacted_line = re.sub(ipv6, self.block, line,flags=re.IGNORECASE)

        return redacted_line

    def process_file(self, filename, option=str, savedir="./"):
        """Function to process supplied file from cli.
        Args:
            filename (str): File to redact
            savedir (str): [Optional] directory to place results

        Returns:
            None
        """
        count = 0
        try:
            with open(filename, encoding="utf-8") as target_file:
                # content = target_file.read()
                if savedir != "./" and savedir[-1] != "/":
                    savedir = savedir + "/"

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

                with open(
                    f"{savedir}redacted_{os.path.basename(filename)}",
                    "w",
                    encoding="utf-8",
                ) as result:

                    if type(option) is not str:
                        print(f"[ + ] No option supplied, will be redacting all the sensitive data supported")
                        for line in target_file:
                            for p in id_object.regexes:
                                if re.search(p['pattern'], line, re.IGNORECASE):
                                    line = re.sub(p['pattern'], self.block, line,
                                                flags=re.IGNORECASE)
                            result.write(line)
                    else:
                        print(f"[ + ] Redacting {option} from the file")
                        for line in target_file:
                            line = self.redact(line,option)
                            result.write(line)
                        
                    print(f"[ + ] Redacted results saved to {savedir}redacted_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[ - ] Removed incomplete redact file")
            sys.exit("[ - ] Unable to read file")
