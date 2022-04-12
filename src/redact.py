import numpy
from nltk.corpus import wordnet as wn
from commonregex import CommonRegex
import nltk
import tempfile
import re
import urllib

```Main redactor library```


class redactor:
    """Redactor class
    Class containing all methods to support redaction
    of sensitive data
    """

    def __init__(self, redactfile=None) -> None:
        """ 
        Class Initialization
        Args:
            redactfile (str): Redactfile name

        Returns:
            None 
        """

    def dates(data):
        """ Identify dates and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            dates_list: array of dates identified from the supplied data
        """
        parsed_text = CommonRegex(data)
        dates_list = parsed_text.dates

        return data, dates_list

    def names(data):
        """ Identify names and return them from the supplied data
        Args:
            data (str): data in alpha-numeric format

        Returns:
            data (str): data in alpha-numeric format
            dates_list: array of dates identified from the supplied data
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
