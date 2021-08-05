"""
Class which collects information about requests and responses
"""

from __future__ import absolute_import
import time
import sys
from mitmproxy import http

from utilities import util
from utilities.util import root_dir
from analysis.analysis import Analysis

sys.path.append(root_dir())


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses during collection phase
    :param flow: active http flow
    :return: -
    """
    print("response")
    if util.correct_filetype(flow):
        Sample(flow)


class Sample:
    """
    Sample object
    """

    def __init__(self, flow):
        """
        Initialise the collection object
        """
        self._sample = None
        self._flow = flow
        self._url = flow.request.pretty_url
        self._filename = str(time.time())
        self._path = None
        self.set_path()
        self.call_analysis()

    def get_path(self):
        """
        Get the path of the file
        :param self:
        :return: the path of the file
        """
        return self._path

    def set_path(self):
        """
        Set the path of the file
        :param self:
        :return:
        """
        self._path = util.to_disk(self._flow, self._filename)

    def call_analysis(self):
        """
        Calls the analysis class
        :param self:
        :return:
        """
        Analysis(self.get_path())
