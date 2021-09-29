"""
Test Collection Phase
"""
from __future__ import absolute_import
import os
from mitmproxy import io, http
from mitmproxy.exceptions import FlowReadException

from collection.collection import Collection
from utilities import response, util
from utilities.response import Response
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


def test_content_type():
    flow = load_flow(root_dir() + "flowInfo.txt")
    # collection = Collection(flow, root_dir() + "/data/samples/dev.unshielded.red")
    assert util.check_content_type(flow)


def test_filename():
    flow = load_flow(root_dir() + "flowInfo.txt")
    collection = Collection(flow)
    response_filename = Collection(flow).get_filename()
    assert len(response_filename) == 18


def test_response_unedited():
    flow = load_flow(root_dir() + "flowInfo.txt")
    collection = Collection(flow)
    collection_response = open(root_dir() + collection.get_path())
    expected_response = open(root_dir() + 'data/outputs/expected/collection.txt')
    assert collection_response == expected_response


if __name__ == "__main__":
    test_filename()
    test_content_type()
    test_response_unedited()
