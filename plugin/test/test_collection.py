"""
Test Collection Phase
"""
import os
from utilities.response import Response
from utilities.request import Request
import re


class collectionTest:

    def __init__(self, test_directory):
        self.filePath = test_directory
        self.requestFiles = []
        self.responseFiles = []
        self._request = None
        self._response = None
        self._filename = None
        self._path = "collection_saving_tests"
        self.index = 0

        filenames = os.listdir(test_directory)
        os.chdir(test_directory)
        for f in filenames:
            file = open(f)
            if f.endswith("request.txt"):
                self.requestFiles.append(file)
            elif f.endswith("response.txt"):
                self.responseFiles.append(file)
            file.close()

        for i in range(len(self.requestFiles)):
            self.index = i
            self.collection_test(self.requestFiles[i], self.responseFiles[i])

    def collection_test(self, test_request_file, test_response_file):
        """
        Initialise the collection object
        """
        self._response = Response(test_response_file)
        self._filename = self._response.get_time()
        self.test_filename()
        self.test_content_match()

    def test_filename(self):
        """
        Tests that filename syntax matches previously saved files
        :return: if filename follows syntax
        """

        assert len(self._filename) == 18

        # if len(self._filename) == 18:
        #     print("Filename matches syntax")

    def test_content_match(self):
        """
        Tests that the contents of the response and requests objects are
        the same as initial test data
        :return: if contents match test data
        """
        # if self._response.get_response() == self.responseFiles[self.index]:
        #     print("Content matches")
        assert self._response.get_response() == self.responseFiles[self.index]


# if __name__ == "__main__":
#     collectionTest("../data/samples/dev.unshielded.red")
