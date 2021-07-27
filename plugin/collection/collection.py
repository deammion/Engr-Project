from mitmproxy import http
import time

import os

from analysis.analysis import Analysis


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses
    :param flow:
    :return:
    """
    print("response")
    url = flow.request.pretty_url
    if not url.endswith(".css") and not url.endswith(".js") and not url.endswith(".jpg") and not url.endswith(".png"):
        Sample(flow)


class Sample:
    """
    Sample object contains individual sample data
    """

    def __init__(self, flow):
        self._sample = None
        self._flow = flow
        self._url = flow.request.pretty_url
        self._path = None
        self._file_name = str(time.time())
        self.to_disk()
        self.call_analysis()

    def get_path(self):
        return self._path

    def set_path(self, x):
        self._path = x

    def call_analysis(self):
        Analysis(self.get_path())

    def to_disk(self):
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
