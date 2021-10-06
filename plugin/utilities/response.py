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
        Initialisation of the response information
        """
        self.flow = flow
        self.time = str(time.time())
        self.content = flow.response.text

    def get_time(self):
        """
        Getter method that gets the time for the response
        :return: the time of the response as a string
        """
        return self.time

    def get_response(self):
        """
        Getter method that gets the response flow
        :return: Response flow
        """
        return self.flow

    def get_response_content(self):
        """
        Getter method that gets the response content
        :return: Response content
        """
        return self.content
