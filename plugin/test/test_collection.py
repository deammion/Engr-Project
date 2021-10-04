"""
Test Collection Phase
"""
from __future__ import absolute_import

from collection.collection import Collection
from utilities import util
from utilities.util import root_dir


def test_content_type():
    """
    Tests that collection is saving the correct content type
    """
    flow = util.load_flow(root_dir() + "/flowInfo.txt")
    assert util.check_content_type(flow)


def test_filename():
    """
    Tests the filename sizes matches what should be epected
    """
    flow = util.load_flow(root_dir() + "/flowInfo.txt")
    response_filename = Collection(flow).get_filename()
    assert len(response_filename) >= 15


def test_response_unedited():
    """
    Tests that the collected response matches the expected response
    """
    flow = util.load_flow(root_dir() + "/flowInfo.txt")
    collection_response = open(Collection(flow).get_path() + Collection(flow).get_filename(), 'r')
    expected_response = open(root_dir() + '/data/outputs/expected/collection.txt', 'r')
    assert len(collection_response.readlines()) == len(expected_response.readlines())
    for response_line in collection_response.readlines():
        assert response_line == expected_response.readlines().pop()


if __name__ == "__main__":
    test_filename()
    test_content_type()
    test_response_unedited()
