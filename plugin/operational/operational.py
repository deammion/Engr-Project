from mitmproxy import http


class Monitor:
    """
    Monitor object contains whitelisted & blacklisted scripts as well as a flow to watch
    """

    def __init__(self, whitelist, blacklist):
        self._whitelist = whitelist
        self._blacklist = blacklist
        self._flow = None


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on requests
    :param flow:
    :return:
    """
    print("response")
