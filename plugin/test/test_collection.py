"""
Test Collection Phase
"""
from __future__ import absolute_import

from mitmproxy import io, http
from mitmproxy.exceptions import FlowReadException

from collection.collection import Collection
from utilities import util
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
    """
    Tests that collection is saving the correct content type
    """
    flow = load_flow(root_dir() + "/flowInfo.txt")
    assert util.check_content_type(flow)


def test_filename():
    """
    Tests the filename sizes matches what should be epected
    """
    flow = load_flow(root_dir() + "/flowInfo.txt")
    response_filename = Collection(flow).get_filename()
    assert len(response_filename) >= 15


def test_response_unedited():
    """
    Tests that the collected response matches the expected response
    """
    flow = load_flow(root_dir() + "/flowInfo.txt")
    collection_response = open(Collection(flow).get_path() + Collection(flow).get_filename(), 'r')
    expected_response = open(root_dir() + '/data/outputs/expected/collection.txt', 'r')
    assert len(collection_response.readlines()) == len(expected_response.readlines())
    for response_line in collection_response.readlines():
        assert response_line == expected_response.readlines().pop()


if __name__ == "__main__":
    test_filename()
    test_content_type()
    test_response_unedited()
