"""
    Corresponds to collection object.
    Runs the analysis phase and saves data to file
    """
from __future__ import absolute_import
from __future__ import division

import time
from builtins import round
import os
import bs4
import re


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
        self.htmls_checked = 0
        self.database_size = 0
        self.update_data = False
        self.scripts = []
        self.db_scripts = []
        self.filenames = []
        self.filenames_sorted = []
        self.db_script_to_count = {}
        self.script_to_count = {}
        self.check_for_database()
        self.read_directory()
        self.parse_htmls(self.filenames)
        self.get_script_count()
        self.write_to_file()

    def check_for_database(self):
        """
        Checks if there is a data.txt file, calls appropriate methods if there is
        :return:
        """
        os.chdir(self.html)
        for file in os.listdir():
            if file.endswith("data.txt"):
                self.update_data = True
                self.get_html_occurrence(file)
                self.get_database_scripts(file)

    def get_html_occurrence(self, file):
        """
        Gets the total times the HTML has been captured from data.txt
        :param file:
        :return:
        """
        text = open(file)
        occurrence_str = text.readline()
        data = occurrence_str.split(" ")
        self.htmls_checked = int(data[1])
        #self.htmls_checked = int(re.search(r'/d+', occurrence_str).group())

    def get_database_scripts(self, file):
        """
        reads the data.txt file, and turns it into a dictionary
        :param file:
        :return:
        """
        with open(file) as f:
            # skip first line i.e HTML occurrence
            next(f)
            self.db_scripts = f.readline()
        for entry in self.db_scripts:
            # new array to sort the frequency and the percentage
            freq_per = []
            script_tag = re.findall('(<script.+?</script>)', entry.strip())
            # remove script tag from entry for ease of parsing
            new_entry = {entry.replace(str(script_tag), '')}
            # finds ints in remaining string
            for word in new_entry:
                if isinstance(word, int):
                    freq_per.append(int(word))
            # freq_per.pop should get first number i.e. the frequency
            self.db_script_to_count.update({script_tag: freq_per.pop()})

    # opens all files, calls get_tags - stand in function
    # change to search for existing doc, if yes - convert to dictionary(MAP)
    def read_directory(self):
        """
        Read all response text files in the given directory
        :return:
        """
        os.chdir(self.html)
        self.database_size = len([name for name in os.listdir('.') if os.path.isfile(name)])
        for file in os.listdir():
            if not file.endswith("data.txt"):
                self.filenames.append(str(file))

    def parse_htmls(self, filenames):
        # sorts the filenames by timestamp, maybe in wrong order
        # TODO test order
        self.filenames_sorted = sorted(filenames, key=lambda x: time.time(), reverse=True)
        if self.update_data:
            # if data.txt file exists, gets the latest HTML first and calls get_tags
            while self.htmls_checked < self.database_size:
                filename = self.filenames_sorted.pop()
                file = f"{os.getcwd()}/{filename}"
                self.get_tags(file)
        else:
            for filename in filenames:
                file = f"{os.getcwd()}/{filename}"
                self.get_tags(file)

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
        self.htmls_checked += 1

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

        # merges db_script_to_count and script_to_count if required
        # TODO - check merge occurs correctly
        if self.update_data:
            for key in self.script_to_count:
                if key in self.db_script_to_count:
                    self.script_to_count[key] = self.db_script_to_count[key] + self.script_to_count[key]
                else:
                    pass

    def write_to_file(self):
        """
        Write Script data (frequency and probability)to file
        :return:
        """
        file = open("data.txt", "w+")
        file.write("HTML Occurrence: " + str(self.htmls_checked) + "\n")
        for key in self.script_to_count:
            file.write(key + " Frequency: " + str(self.script_to_count[key]) +
                       " Probability: " + str(
                round((self.script_to_count[key] / (len(os.listdir(
                    self.html)) - 1)) * 100, 2)) + "%" + "\n")
        file.close()
