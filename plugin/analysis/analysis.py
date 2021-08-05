"""
    Corresponds to collection object.
    Runs the analysis phase and saves data to file
    """
from __future__ import absolute_import
from __future__ import division

from builtins import round
import os
import bs4


class Analysis:
    """
        Corresponds to collection object.
        Runs the analysis phase and saves data to file
        """

    def __init__(self, html):
        """
            Runs analysis object
            """
        self.html = html
        self.scripts = []
        self.script_to_count = {}
        self.read_directory()
        self.get_script_count()
        self.write_to_file()

    # opens all files, calls get_tags - stand in function
    # change to search for existing doc, if yes - convert to dictionary(MAP)
    def read_directory(self):
        """
        Read all response text files in the given directory
        :return:
        """
        os.chdir(self.html)
        for file in os.listdir():
            if not file.endswith("data.txt"):
                read = f"{os.getcwd()}/{file}"
                self.get_tags(read)

    # find all script tags store to array
    def get_tags(self, file):
        """
        Identify & strip tags from response files
        :return:
        """
        print("Reading File: " + file)
        response = open(file)

        text = response.read()
        soup = bs4.BeautifulSoup(text, features='html.parser')
        scripts = soup.find_all('script')
        if scripts:
            for script in scripts:
                self.scripts.append(str(script))

        response.close()

    # count all script tags in scripts, assign to dictionary(map in java)
    def get_script_count(self):
        """
        Calculate the frequency of a script
        :return:
        """
        i = 0
        while i < len(self.scripts):
            count = self.scripts.count(self.scripts[i])
            self.script_to_count.update({self.scripts[i]: count})
            i += 1

    def write_to_file(self):
        """
        Write Script data (frequency and probability)to file
        :return:
        """
        file = open("data.txt", "w+")
        for key in self.script_to_count:
            file.write(key + " Frequency: " + str(self.script_to_count[key]) +
                       " Probability: " + str(
                           round((self.script_to_count[key] / (len(os.listdir(
                               self.html)) - 1)) * 100, 2)) + "%" + "\n")
        file.close()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     """
#             Run analysis on all files in the sample data directory
#             :return:"""
#     Analysis('../data/samples/dev.unshielded.red')

