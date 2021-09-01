class request:

    def __init__(self,flow):
        self.flow = flow
        self.url = flow.request.pretty_url

    def getUrl(self):
        return self.url

    def correct_filetype(self):
        """
        Check file extension matches allowed types
        :param flow: http flow to check file extensions upon
        :return: True if extension matches allowed type
        """
        if not (self.url.endswith(".css") or
                self.url.endswith(".jpg") or
                self.url.endswith(".png") or
                self.url.endswith(".js") or
                self.url.__contains__("www.gstatic.com")):
            return True
        return False


