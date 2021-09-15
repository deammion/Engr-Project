"""
Data node class
"""
from __future__ import division


class DataNode:

    def __init__(self, s, f, h):
        """
            Data object fields
            """
        self.script = s
        self.frequency = f
        self.htmls_checked = h
        self.probability = round((f / h) * 100, 2)

    """
            Gets the script associated with the data node
            """

    def get_script(self):
        return self.script

    """
            Gets the script frequency of the data node
            """

    def get_frequency(self):
        return self.frequency

    """
            Gets the script probability of the data node
            """

    def get_probability(self):
        return self.probability

    """
            sets the script frequency of the data node
            """

    def set_frequency(self, f):
        self.frequency = f
        self.probability = round((f / self.htmls_checked) * 100, 2)

    """
            sets the htmls checked of the data node
            """

    def set_htmls_checked(self, html):
        self.htmls_checked = html
        self.probability = round((self.frequency / html) * 100, 2)

    """
            To string that is used for writing data to data.txt
            """

    def to_string(self):
        return self.script + " Frequency: " + str(self.frequency) \
               + " Probability: " + str(self.probability) + "%" + "\n"
        # return "==============================" + "\n" + self.script + "\n" + " Frequency: " + str(self.frequency) \
        #        + "\n" + " Probability: " + str(self.probability) + "%" + "\n"
