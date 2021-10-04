"""
Class which stores and processes the request information
"""


class Request:
    """
    Request object
    """

    def __init__(self, flow):
        """
        Initialise the Request information
        """
        self.flow = flow
        self.url = flow.request.pretty_url
        self.headers = flow.request.headers.items()

    def get_url(self):
        """
        Get the url associated with the request
        :return: The request URL
        """
        return self.url

    def correct_filetype(self):
        """
        Check file extension matches allowed types
        :return: True if extension matches allowed type
        """
        if not (self.url.endswith(".css") or
                self.url.endswith(".jpg") or
                self.url.endswith(".png") or
                self.url.endswith(".js") or
                self.url.__contains__("www.gstatic.com")):
            return True
        return False
