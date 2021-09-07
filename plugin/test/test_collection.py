"""
Test Collection Phase
"""
import os
from utilities.response import Response


class CollectionTest:

    def __init__(self, test_directory):
        self.file_path = test_directory
        self.request_files = []
        self.response_files = []
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
                self.request_files.append(file)
            elif f.endswith("response.txt"):
                self.response_files.append(file)
            file.close()

        for i in range(len(self.request_files)):
            self.index = i
            self.collection_test(self.request_files[i], self.response_files[i])

    def collection_test(self, test_request_file, test_response_file):
        """
        Initialise the collection object
        """
        self._request = test_request_file
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
        assert self._response.get_response() == self.response_files[self.index]


# if __name__ == "__main__":
#     CollectionTest("../data/samples/dev.unshielded.red")
