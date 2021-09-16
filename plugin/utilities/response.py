"""
Class which stores and processes the response information
"""

from __future__ import absolute_import
import time


class Response:
    """
    Response object
    """

    def __init__(self, flow):
        """
        Initialise the response information
        """
        self.flow = flow
        self.time = str(time.time())
        self.headers = flow.response.headers.items()

    def get_time(self):
        """
        Get the time fo the response
        :return: the time of the response as a string
        """
        return self.time

    def get_response(self):
        """
        Get the response flow
        :return: The response flow
        """
        return self.flow

    def get_response_content(self):
        """
        Get the response content
        :return: The response content
        """
        return self.flow.response.headers + "\n" + self.flow.response.text
