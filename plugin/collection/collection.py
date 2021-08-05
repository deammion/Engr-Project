from mitmproxy import http
import time
import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from analysis.analysis import Analysis

"""
Class which collects information about requests and responses
"""

def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses
    :param flow:
    :return:
    """
    print("response")
    url = flow.request.pretty_url
    if not url.endswith(".css") and not url.endswith(".js") and not url.endswith(".jpg") and not url.endswith(".png")\
            and not url.__contains__("www.gstatic.com"):
        Sample(flow)

class Sample:
    """
    Sample object contains individual sample data
    """

    def __init__(self, flow):
        """
        Initialise the collection object
        """
        self._sample = None
        self._flow = flow
        self._url = flow.request.pretty_url
        self._path = None
        self._file_name = str(time.time())
        self.to_disk()
        self.call_analysis()

    def get_path(self):
        """
        Get the path of the file
        :param self:
        :return: the path of the file
        """
        return self._path

    def set_path(self, file_path):
        """
        Set the path of the file
        :param self:
        "param file_path:
        :return:
        """
        self._path = file_path

    def call_analysis(self):
        """
        Calls the analysis class
        :param self:
        :return:
        """
        Analysis(self.get_path())

    def to_disk(self):
        """
        Saves information to a file on the disk
        :param self:
        :return:
        """
        data = self._url.split("/")
        data = data[2:]
        root_path = os.getcwd()
        for folder in data:
            root_path = os.path.join(root_path, folder)
            if not os.path.exists(root_path):
                os.mkdir(root_path)
        self.set_path(root_path)
        file_path = os.path.join(root_path, self._file_name)
        file = open(file_path, "w")
        file.write(self._flow.response.text + "\n")
        file.close()
