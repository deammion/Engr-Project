from mitmproxy import http
import uuid


class Collection:
    """
    Collection object contains individual sample data
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
    Run automatically by mitmproxy on requests
    :param flow:
    :return:
    """
    print("request")
    Collection(flow)


def collate():
    """
    Collate collected samples/get dir path
    :return: Path to sample container
    """
    return 1
