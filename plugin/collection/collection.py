from mitmproxy import http
import uuid
import os
from analysis.analysis import Analysis
from utilities.util import print_header


class Sample:
    """
    Sample object contains individual sample data
    """

    def __init__(self, flow):
        self._sample = None
        self._flow = flow
        self._path = None

    def get_path(self):
        return self._path

    def set_path(self, x):
        self._path = x

    def toDisk(self):
        file = open(str(uuid.uuid4()), "a")
        file.write(self._flow.request.pretty_url + "\n")
        file.close()


def request(flow: http.HTTPFlow) -> None:
    """
    Run automatically by mitmproxy on requests
    :param flow:
    :return:
    """
    print("request")
    s = Sample(flow)
    s.toDisk()
    s.set_path("plugin/data/samples/dev.unshielded.red/1-request.txt")

    try:
        print_header("STARTING ANALYSIS")
        Analysis(s.get_path())
    except IndexError as e:
        print("Error analysing samples ", e)


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses
    :param flow:
    :return:
    """
    print("response")
    url = flow.request.pretty_url
    if not url.endswith(".css") and not url.endswith(".js") and not url.endswith(".jpg"):
        data = url.split("/")
        data = data[2:]
        root_path = os.getcwd()
        for folder in data:
            root_path = os.path.join(root_path, folder)
            if not os.path.exists(root_path):
                os.mkdir(root_path)

    file = open("html.txt", "a")
    file.write(flow.response.text + "\n")
    file.close()
    print(flow.request.pretty_url)
