"""
Test Operation Phase
"""

from __future__ import absolute_import
import os

from operational.operational import Operational
from utilities.util import root_dir

from mitmproxy import io, http
from mitmproxy.exceptions import FlowReadException


def load_flow(filename):
    """
    Create a method to load a flow so the operation class can be created
    """
    with open(filename, "rb") as logfile:
        freader = io.FlowReader(logfile)
        try:
            for f in freader.stream():
                if isinstance(f, http.HTTPFlow):
                    return f
        except FlowReadException as e:
            print(f"Flow file corrupted: {e}")


def test_match():
    """
    Create a test to check that nonce tags are correctly added to all safe script tags
    """
    flow = load_flow(root_dir() + '\\flowInfo.txt')
    operational = Operational(flow, root_dir() + '/data/outputs/actual/operationalOutput')
    operational._nonce = "THIS_IS_NONCE"

    # write the created output to a file for later comparison
    f = open(root_dir() + '/data/outputs/actual/operational.txt', "w")
    f.write(operational.add_nonce_to_html())
    f.close()

    # read both the expected and actual files to compare them
    expected = open(os.path.join(root_dir(), 'data/outputs/expected/operational.txt')).read()
    actual = open(os.path.join(root_dir(), 'data/outputs/actual/operational.txt')).read()

    if expected == actual:
        assert True
    else:
        assert False


test_match()

