"""
Test Operation Phase
"""

from __future__ import absolute_import
import os
from mitmproxy import io, http
from mitmproxy.exceptions import FlowReadException

from operational.operational import Operational
from utilities.util import root_dir


def load_flow(filename):
    """
    Create a method to load a flow so the operation class can be created
    Code taken directly from https://docs.mitmproxy.org/stable/addons-examples/
    :param filename: file name of the file to load
    :return: the flow
    """
    with open(filename, "rb") as logfile:
        f_reader = io.FlowReader(logfile)
        try:
            for flow in f_reader.stream():
                if isinstance(flow, http.HTTPFlow):
                    return flow
        except FlowReadException as exception:
            print(f"Flow file corrupted: {exception}")
    return None


def test_match():
    """
    Create a test to check that nonce tags are correctly added to all safe script tags
    """
    flow = load_flow(root_dir() + '\\flowInfo.txt')
    operational = Operational(flow, root_dir() + '/data/outputs/actual/operationalOutput')
    operational.set_nonce("THIS_IS_NONCE")

    # write the created output to a file for later comparison
    file = open(root_dir() + '/data/outputs/actual/operational.txt', "w")
    file.write(operational.add_nonce_to_html())
    file.close()

    # read both the expected and actual files to compare them
    expected = open(os.path.join(root_dir(), 'data/outputs/expected/operational.txt')).read()
    actual = open(os.path.join(root_dir(), 'data/outputs/actual/operational.txt')).read()

    if expected == actual:
        assert True
    else:
        assert False


test_match()
