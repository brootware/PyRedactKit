""" Main redactor class implementation """
from unittest import case
from nltk.corpus import wordnet as wn
from commonregex import CommonRegex
import nltk
import os
import mimetypes
import re
import sys

""" Main redactor library """


class Redactor:
    """Redactor class
    Class containing all methods to support redaction
    of sensitive data

    Static variables:
        block (unicode string): To redact sensitive data
    """
    block = '\u2588'

    def __init__(self, redactfile=None) -> None:
        """ 
        Class Initialization
        Args:
            redactfile (str): Redactfile name

        Returns:
            None 
        """

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

    def names(data):
        """ Identify names and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            dates_list (array): array of names identified from the supplied data
        """
        name = ""
        name_list = []
        words = nltk.word_tokenize(data)
        part_of_speech_tagsets = nltk.pos_tag(words)
        named_ent = nltk.ne_chunk(part_of_speech_tagsets, binary=False)

        for subtree in named_ent.subtrees():
            if subtree.label() == 'PERSON':
                l = []
                for leaf in subtree.leaves():
                    l.append(leaf[0])
                name = ' '.join(l)
                if name not in name_list:
                    name_list.append(name)

        return data, name_list

    def dates(data):
        """ Identify dates and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            dates_list (array): array of dates identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        dates_list = parsed_text.dates

        return data, dates_list

    def phones(data):
        """ Identify phones and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            total_phones_list (array): array of phones identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        phones_list = parsed_text.phones
        phones_ext_list = parsed_text.phones_with_exts

        total_phones_list = phones_list + phones_ext_list
        return data, total_phones_list

    def dns_strings(data):
        """ Identify dns and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            dns_list (array): array of dns strings identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        dns_list = parsed_text.links

        return data, dns_list

    def emails(data):
        """ Identify emails and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            emails_list (array): array of emails strings identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        emails_list = parsed_text.emails

        return data, emails_list

    def ipv4_addresses(data):
        """ Identify ipv4 addresses and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            ipv4_list (array): array of ipv4 addresess identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        ipv4_list = parsed_text.ips

        return data, ipv4_list

    def ipv6_addresses(data):
        """ Identify ipv4 addresses and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            ipv6_list (array): array of ipv6 addresess identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        ipv6_list = parsed_text.ipv6s

        return data, ipv6_list

    def credit_cards(data):
        """ Identify ipv4 addresses and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            cc_list (array): array of credit card numbers identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        cc_list = parsed_text.credit_cards()

        return data, cc_list

    def to_redact(self, redact_list=[]):
        """ Helper function that takes in list of keywords to be redacted from data.
        Args:
            redact_list (array): data in alpha-numeric format

        Returns:
            data (str): redacted data

        """
        for elm in redact_list:
            total_elm = len(elm)
            # encode element to be blocked
            elm = r'\b' + elm + r'\b'
            # multiply the block with length of identified elements
            bl = total_elm * self.block
            # substitute the block using regular expression
            data = re.sub(elm, bl, data)

        return data

    def redact(self, data=str, option=str):
        """ Main function to redact
        Args:
            data (str) : data to be supplied to redact
            option (str): (optional) choice for redaction

        Returns:
            redacted_data (str): redacted data
        """
        if option == "names":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            names_list = self.names(data)
            redacted_data = self.to_redact(name_list)
        elif option == "dates":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            dates_list = self.dates(data)
            redacted_data = self.to_redact(dates_list)
        elif option == "phones":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            phones_list = self.phones(data)
            redacted_data = self.to_redact(phones_list)
        elif option == "dns":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            dns_list = self.dns_strings(data)
            redacted_data = self.to_redact(dns_list)
        elif option == "emails":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            emails_list = self.emails(data)
            redacted_data = self.to_redact(emails_list)
        elif option == "ipv4":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            ipv4_list = self.ipv4_addresses(data)
            redacted_data = self.to_redact(ipv4_list)
        elif option == "ipv6":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            ipv6_list = self.ipv6_addresses(data)
            redacted_data = self.to_redact(ipv6_list)
        elif option == "cc":
            return f"[ + ] Redacting {option} from the file. This might take some time"
            cc_list = self.credit_cards(data)
            redacted_data = self.to_redact(cc_list)
        else:
            return f"[ + ] No option supplied, will be redacting all the sensitive data supported"
            all_sensi = self.names(data) + self.dates(data) + self.phones(data) + self.dns_strings(data) + self.emails(data) + \
                self.ipv4_addresses(
                    data) + self.ipv6_addresses(data) + self.credit_cards(data)
            redacted_data = self.to_redact(all_sensi)

        return redacted_data

    def process_file(self, filename, option=str, savedir='./'):
        """ Function to process supplied file from cli.
        Args:
            filename (str): File to redact
            savedir (str): [Optional] directory to place results

        Returns:
            None
        """
        try:
            with open(filename, encoding="utf-8") as target_file:
                if savedir != "./" and savedir[-1] != "/":
                    savedir = savedir + "/"

                if not os.path.exists(os.path.dirname(savedir)):
                    print("[ + ] " + os.path.dirname(savedir) +
                          " directory does not exist, creating it.")
                    os.makedirs(os.path.dirname(savedir))

                print(
                    "[ + ] Processing starts now. This may take some time depending on file size.")

                with open(f"{savedir}redacted_{os.path.basename(filename)}", 'w', encoding="utf-8") as result:
                    for line in target_file:
                        data = self.redact(line, option)
                    result.write(data)
        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[ - ] Removed incomplete redact file")
            sys.exit("[ - ] Unable to read file")
