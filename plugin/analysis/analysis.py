"""
    Corresponds to collection object.
    Runs the analysis phase and saves data to file
    """
from __future__ import absolute_import
from __future__ import division

import os
import bs4

from utilities.data_node import DataNode


class Analysis:
    """
        Corresponds to collection object.
        Runs the analysis phase and saves data to file
        """

    DATA_FILENAME = "data.txt"
    READABLE_DATA_FILENAME = "readable_data.txt"

    def __init__(self, file_path):
        """
            Runs analysis object
            """
        self.file_path = file_path
        self.htmls_checked = 0
        self.update_data = False
        self.scripts = []
        self.filenames_sorted = []
        self.db_script_to_count = {}
        self.script_to_count = {}
        self.analyse_data()

    def analyse_data(self):
        """
        Method to call the appropriate methods
        """
        if os.path.isfile(self.file_path + "/" + self.DATA_FILENAME):
            self.update_data = True
            self.get_html_occurrence()
            self.get_database_scripts()

        self.read_directory()

        if not self.htmls_checked == len(self.filenames_sorted):
            self.parse_htmls()
            self.get_script_count()
            self.write_to_file()

    def get_html_occurrence(self):
        """
        Gets the total times the HTML has been captured from data.txt
        :return:
        """
        text = open(self.file_path + "/" + self.DATA_FILENAME)
        occurrence_str = text.readline()
        data = occurrence_str.split(":")
        self.htmls_checked = int(data[1])
        text.close()

    def get_database_scripts(self):
        """
        reads the data.txt file, and turns it into a dictionary
        :return:
        """
        file = open(self.file_path + "/" + self.DATA_FILENAME)
        # ignore the first line which is the HTML occurrence
        next(file)
        lines = file.readlines()
        file.close()

        for line in lines:
            soup = bs4.BeautifulSoup(line, features='html.parser')
            script = soup.find('script')

            # find frequency in remaining string
            data = line.split("Frequency: ")
            data = data[1].split(" ")

            if data[0].isdigit():
                # add the script with its frequency to the map
                # self.data_nodes.append(DataNode(str(script), int(data[0]), self.htmls_checked))
                self.db_script_to_count.update({str(script): int(data[0])})

    def read_directory(self):
        """
        Read all response text files in the given directory
        :return:
        """
        filenames = os.listdir(self.file_path)

        if self.DATA_FILENAME in filenames:
            filenames.remove(self.DATA_FILENAME)
        if self.READABLE_DATA_FILENAME in filenames:
            filenames.remove(self.READABLE_DATA_FILENAME)

        filenames_floats = []
        for filename in filenames:
            if not os.path.isdir(self.file_path + "/" + filename):
                filenames_floats.append(float(filename))

        filenames = sorted(filenames_floats)

        for filename in filenames:
            self.filenames_sorted.append(str(filename))

    def parse_htmls(self):
        """
        Parse the script tags in all the files
        """
        if self.update_data:
            num_files = len(self.filenames_sorted)

            # if data.txt file exists, gets the latest HTML first and calls get_tags
            while self.htmls_checked < num_files:
                filename = self.filenames_sorted.pop()
                file = self.file_path + "/" + filename
                self.get_tags(file)
        else:
            for filename in self.filenames_sorted:
                file = self.file_path + "/" + filename
                self.get_tags(file)

    def get_tags(self, file):
        """
        Identify & strip tags from response files
        :param file:
        :return:
        """
        print("Reading File: " + file)
        response = open(file, mode="r", encoding="utf-8", errors='ignore')
        text = response.read()
        text = text.replace('\n', '')
        text = text.replace('\t', '')

        soup = bs4.BeautifulSoup(text, features='html.parser')
        scripts = soup.find_all('script')
        if scripts:
            for script in scripts:
                self.scripts.append(str(script))

        response.close()
        self.htmls_checked += 1
        # for data in self.data_nodes:
        #     data.set_htmls_checked(self.htmls_checked)

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
        if self.update_data:
            for key in self.script_to_count:
                if key in self.db_script_to_count:
                    self.script_to_count[key] = self.db_script_to_count[key] \
                                                + self.script_to_count[key]
                else:
                    pass

    def write_to_file(self):
        """
        Write Script data (frequency and probability)to file
        :return:
        """
        file = open(self.file_path + "/" + self.READABLE_DATA_FILENAME, "w+")
        data_nodes = []
        file.write("HTML Occurrence: " + str(self.htmls_checked) + "\n")
        for key in self.script_to_count:
            data_nodes.append(DataNode(key, self.script_to_count[key], self.htmls_checked))
        for nodes in data_nodes:
            file.write(nodes.to_string())
        file.close()

        file = open(self.file_path + "/" + self.DATA_FILENAME, "w+")
        file.write("HTML Occurrence: " + str(self.htmls_checked) + "\n")
        for key in self.script_to_count:
            file.write(key + " Frequency: " + str(self.script_to_count[key])
                       + " Probability: " + str(round((self.script_to_count[key] /
                                                       self.htmls_checked) * 100, 2)) + "%" + "\n")
        file.close()


if __name__ == "__main__":
    Analysis("../data/samples/script_tags_sample")