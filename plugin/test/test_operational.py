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

