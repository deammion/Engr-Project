"""
Test Collection Phase
"""
from __future__ import absolute_import
import os
from utilities.response import Response


class CollectionTest:
    """
            Corresponds to collection testing object.
            Runs the file name and response gathering parts of collection
            """

    def __init__(self, test_directory):
        self.file_path = test_directory
        self.request_files = []
        self.response_files = []
        self._request = None
        self._response = None
        self._filename = None
        self._path = "collection_saving_tests"
        filenames = os.listdir(test_directory)
        os.chdir(test_directory)
        for f in filenames:
            file = open(f)
            if f.endswith("request.txt"):
                self.request_files.append(file)
            elif f.endswith("response.txt"):
                self.response_files.append(file)
            file.close()
        for i in range(len(self.request_files)):
            self.collection_test(self.request_files[i], self.response_files[i], i)

    def collection_test(self, test_request_file, test_response_file, index):
        """
        Initialise the collection object
        """
        self._request = test_request_file
        self._response = Response(test_response_file)
        self._filename = self._response.get_time()
        self.test_filename()
        self.test_content_match(index)

    def test_filename(self):
        """
        Tests that filename syntax matches previously saved files
        :return: if filename follows syntax
        """
        # if len(self._filename) == 18:
        #     print("Filename matches syntax")
        assert len(self._filename) == 18

    def test_content_match(self, index):
        """
        Tests that the contents of the response and requests objects are
        the same as initial test data
        :return: if contents match test data
        """
        # if self._response.get_response() == self.response_files[index]:
        #     print("Content matches")
        assert self._response.get_response() == self.response_files[index]


if __name__ == "__main__":
    CollectionTest("../data/samples/dev.unshielded.red")
