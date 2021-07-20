from mitmproxy import http
import uuid; uuid.uuid4()


class Collection:
    """
    Collection object contains the collected data
    """

    def __init__(self, flow):
        self._samples = None
        self._flow = flow

    def toDisk(self):
        file = open(str(uuid.uuid4()), "a")
        file.write(self._flow.request.pretty_url + "\n")
        file.close()


def request(flow: http.HTTPFlow) -> None:
    """

    :param flow:
    :return:
    """
    print("request")
    Collection(flow)


def collate():
    return 1
