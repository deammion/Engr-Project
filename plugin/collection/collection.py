from mitmproxy import http
import time

import uuid
import os

def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses
    :param flow:
    :return:
    """
    print("response")
    current_time = time.time()
    url = flow.request.pretty_url
    if not url.endswith(".css") and not url.endswith(".js") and not url.endswith(".jpg") and not url.endswith(".png"):
        data = url.split("/")
        data = data[2:]
        root_path = os.getcwd()
        for folder in data:
            root_path = os.path.join(root_path, folder)
            if not os.path.exists(root_path):
                os.mkdir(root_path)

        file_path = os.path.join(root_path, str(current_time))
        file = open(file_path, "w")
        file.write(flow.response.text + "\n")
        file.close()


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
