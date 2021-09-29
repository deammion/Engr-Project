"""
Class which collects information about requests and responses
"""

from __future__ import absolute_import
import sys
from mitmproxy import http
from analysis.analysis import Analysis
from utilities.response import Response
from utilities.request import Request
from utilities import util
from utilities.util import root_dir

sys.path.append(root_dir())


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses during collection phase
    :param flow: active http flow
    :return: -
    """
    print("response")
    if util.check_content_type(flow):
        Collection(flow)


class Collection:
    """
    Collection object
    """

    def __init__(self, flow):
        """
        Initialise the collection object
        """
        self._request = Request(flow)
        self._response = Response(flow)
        self._filename = self._response.get_time()
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
        self._path = util.to_disk(self._response.get_response(), None, self._filename)

    def get_filename(self):
        return self._filename

    def call_analysis(self):
        """
        Calls the analysis class
        :param self:
        :return:
        """
        Analysis(self.get_path())
