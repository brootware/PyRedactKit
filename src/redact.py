""" Main redactor class implementation """

import mimetypes
import os
import re
import sys
import time
import nltk

""" Main redactor library """


class Redactor:
    """Redactor class
    Class containing all methods to support redaction
    of sensitive data

    Static variables:
        block (unicode string): To redact sensitive data
    """

    block = "\u2588"

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

    def names(self, data):
        """ Identify names and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            name_list (array): array of names identified from the supplied data
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

        return name_list

    def dns_strings(self, data):
        """Identify dns and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            dns_list (array): array of dns strings identified from the supplied data
        """
        parsed_text = re.findall('(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|(?:construction)|(?:contractors)|(?:enterprises)|(?:photography)|(?:immobilien)|(?:management)|(?:technology)|(?:directory)|(?:education)|(?:equipment)|(?:institute)|(?:marketing)|(?:solutions)|(?:builders)|(?:clothing)|(?:computer)|(?:democrat)|(?:diamonds)|(?:graphics)|(?:holdings)|(?:lighting)|(?:plumbing)|(?:training)|(?:ventures)|(?:academy)|(?:careers)|(?:company)|(?:domains)|(?:florist)|(?:gallery)|(?:guitars)|(?:holiday)|(?:kitchen)|(?:recipes)|(?:shiksha)|(?:singles)|(?:support)|(?:systems)|(?:agency)|(?:berlin)|(?:camera)|(?:center)|(?:coffee)|(?:estate)|(?:kaufen)|(?:luxury)|(?:monash)|(?:museum)|(?:photos)|(?:repair)|(?:social)|(?:tattoo)|(?:travel)|(?:viajes)|(?:voyage)|(?:build)|(?:cheap)|(?:codes)|(?:dance)|(?:email)|(?:glass)|(?:house)|(?:ninja)|(?:photo)|(?:shoes)|(?:solar)|(?:today)|(?:aero)|(?:arpa)|(?:asia)|(?:bike)|(?:buzz)|(?:camp)|(?:club)|(?:coop)|(?:farm)|(?:gift)|(?:guru)|(?:info)|(?:jobs)|(?:kiwi)|(?:land)|(?:limo)|(?:link)|(?:menu)|(?:mobi)|(?:moda)|(?:name)|(?:pics)|(?:pink)|(?:post)|(?:rich)|(?:ruhr)|(?:sexy)|(?:tips)|(?:wang)|(?:wien)|(?:zone)|(?:biz)|(?:cab)|(?:cat)|(?:ceo)|(?:com)|(?:edu)|(?:gov)|(?:int)|(?:mil)|(?:net)|(?:onl)|(?:org)|(?:pro)|(?:red)|(?:tel)|(?:uno)|(?:xxx)|(?:ac)|(?:ad)|(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)|(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)|(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|(?:ch)|(?:ci)|(?:ck)|(?:cl)|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|(?:cx)|(?:cy)|(?:cz)|(?:de)|(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:dz)|(?:ec)|(?:ee)|(?:eg)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|(?:ga)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|(?:gm)|(?:gn)|(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:lb)|(?:lc)|(?:li)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)|(?:ma)|(?:mc)|(?:md)|(?:me)|(?:mg)|(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|(?:mu)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|(?:ni)|(?:nl)|(?:no)|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)|(?:ps)|(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:st)|(?:su)|(?:sv)|(?:sx)|(?:sy)|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|(?:tr)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:vg)|(?:vi)|(?:vn)|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:za)|(?:zm)|(?:zw))(?:/[^\s()<>]+[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019])?)', data, flags=re.IGNORECASE)
        dns_list = parsed_text

        return dns_list

    def emails(self, data):
        """Identify emails and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            emails_list (array): array of emails strings identified from the supplied data
        """
        parsed_text = re.findall("([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", data, flags=re.IGNORECASE)
        emails_list = parsed_text

        return emails_list

    def ipv4_addresses(self, data):
        """Identify ipv4 addresses and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            ipv4_list (array): array of ipv4 addresess identified from the supplied data
        """
        parsed_text = re.findall('(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', data, re.IGNORECASE)
        ipv4_list = parsed_text

        return ipv4_list

    def ipv6_addresses(self, data):
        """Identify ipv4 addresses and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            ipv6_list (array): array of ipv6 addresess identified from the supplied data
        """
        parsed_text = re.findall('\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*', data, re.VERBOSE | re.IGNORECASE | re.DOTALL)
        ipv6_list = parsed_text

        return ipv6_list

    def credit_cards(self, data):
        """ Identify ipv4 addresses and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            cc_list (array): array of credit card numbers identified from the supplied data
        """
        parsed_text = re.findall('((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])',data)
        cc_list = parsed_text

        return cc_list

    def to_redact(self, data=str, redact_list=[]):
        """Helper function that takes in list of keywords to be redacted from data.
        Args:
            redact_list (array): list of keywords in alpha-numeric format
            data (str): data to be redacted in alpha-numeric format

        Returns:
            data (str): redacted data
        """
        redact_count = 0
        

        for elm in redact_list:
            # multiply the block with 15 regardless of length
            bl = self.block * 15
            # substitute the block using regular expression
            data = data.replace(elm,bl)
            redact_count += 1

        
        print()
        print(f"[ + ] Redacted {redact_count} targets...")
        return data

    def redact(self, data=str, option=str):
        """Main function to redact
        Args:
            data (str) : data to be supplied to redact
            option (str): (optional) choice for redaction

        Returns:
            redacted_data (str): redacted data
        """
        start = time.time()
        if option == "dns":
            print(
                f"[ + ] Redacting {option} from the file. This might take some time")
            dns_list = self.dns_strings(data)
            redacted_data = self.to_redact(data, dns_list)
        elif option in ("email", "emails"):
            print(
                f"[ + ] Redacting {option} from the file. This might take some time")
            emails_list = self.emails(data)
            redacted_data = self.to_redact(data, emails_list)
        elif option == "ipv4":
            print(
                f"[ + ] Redacting {option} from the file. This might take some time")
            ipv4_list = self.ipv4_addresses(data)
            redacted_data = self.to_redact(data, ipv4_list)
        elif option == "ipv6":
            print(
                f"[ + ] Redacting {option} from the file. This might take some time")
            ipv6_list = self.ipv6_addresses(data)
            redacted_data = self.to_redact(data, ipv6_list)
        elif option == "names":
            print(
                f"[ + ] Redacting {option} from the file. This might take some time")
            name_list = self.names(data)
            redacted_data = self.to_redact(data, name_list)
        elif option == "cc":
            print(
                f"[ + ] Redacting {option} from the file. This might take some time")
            cc_list = self.credit_cards(data)
            redacted_data = self.to_redact(data, cc_list)
        else:
            print(
                "[ + ] No option supplied, will be redacting all the sensitive data supported"
            )
            all_sensi = (
                self.emails(data)
                + self.dns_strings(data)
                + self.ipv4_addresses(data)
                + self.ipv6_addresses(data)
                + self.names(data)
                + self.credit_cards(data)
            )
            redacted_data = self.to_redact(data, all_sensi)
        end = time.time()
        time_taken = end - start
        print(f"[ + ] Took {time_taken} seconds to execute")
        return redacted_data
        

    def process_file(self, filename, option=str, savedir="./"):
        """Function to process supplied file from cli.
        Args:
            filename (str): File to redact
            savedir (str): [Optional] directory to place results

        Returns:
            None
        """
        try:
            with open(filename, encoding="utf-8") as target_file:
                content = target_file.read()
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
                    data = self.redact(content, option)
                    result.write(data)
                    print(f"[ + ] Redacted results saved to {savedir}redacted_{os.path.basename(filename)}")

        except UnicodeDecodeError:
            os.remove(f"{savedir}redacted_{os.path.basename(filename)}")
            print("[ - ] Removed incomplete redact file")
            sys.exit("[ - ] Unable to read file")
