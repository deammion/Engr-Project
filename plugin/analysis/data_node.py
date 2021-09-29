"""
Data node class
"""
from __future__ import absolute_import
from __future__ import division
from builtins import round


class DataNode:
    """
    Data node class
    """

    def __init__(self, s, f, h):
        """
            Data object fields
            """
        self.script = s
        self.frequency = f
        self.htmls_checked = h
        self.probability = round((f / h) * 100, 2)

    def get_script(self):
        """
                    Gets the script associated with the data node
                    """
        return self.script

    def get_frequency(self):
        """
                    Gets the script frequency of the data node
                    """
        return self.frequency

    def get_probability(self):
        """
                    Gets the script probability of the data node
                    """
        return self.probability

    def set_frequency(self, f):
        """
                    sets the script frequency of the data node
                    """
        self.frequency = f
        self.probability = round((f / self.htmls_checked) * 100, 2)

    def set_htmls_checked(self, html):
        """
                    sets the htmls checked of the data node
                    """
        self.htmls_checked = html
        self.probability = round((self.frequency / html) * 100, 2)

    def to_string(self):
        """
                    To string that is used for writing data to data.txt
                    """
        # return self.script + " Frequency: " + str(self.frequency) \
        #        + " Probability: " + str(self.probability) + "%" + "\n"
        return "==============================" + "\n" + self.script + "\n" + "Frequency: " + str(self.frequency) \
               + "\n" + "Probability: " + str(self.probability) + "%" + "\n"
