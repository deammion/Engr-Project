from mitmproxy import http
import time
import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from analysis.analysis import Analysis


class Monitor:
    """
    Object contains individual sample data
       """
    def __init__(self, flow):
        self._sample = None
        self._flow = flow
        self._url = flow.request.pretty_url
        self._path = None
        self._file_name = str(time.time())
        self.to_disk()
        self.calculate_safe_tags()
        self.call_analysis()

    def get_path(self):
        return self._path

    def set_path(self, x):
        self._path = x

    def get_filename(self):
        return self._file_name

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

    def calculate_safe_tags(self):
        print("Calculate Safe Script Tags")


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
        Monitor(flow)
