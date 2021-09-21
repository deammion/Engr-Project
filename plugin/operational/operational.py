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


def test_nonce_tags_added():
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


def test_determines_safe_tags():
    """
    Create a test to check that the program correctly determines which script tags are safe and unsafe
    """
    flow = load_flow(root_dir() + '\\flowInfo.txt')
    operational = Operational(flow, root_dir() + '/data/outputs/actual/operationalOutput')

    actual_safe_scripts = operational.get_scripts()[1]
    actual_unsafe_scripts = operational.get_scripts()[0]

    expected_safe_scripts = ['<script src="assets/js/jquery-3.3.1.min.js"></script>',
                             '<script src="assets/js/jquery-migrate-3.0.0.min.js"></script>',
                             '<script crossorigin="anonymous" '
                             'integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" '
                             'src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js">'
                             '</script>',
                             '<script crossorigin="anonymous" '
                             'integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" '
                             'src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>',
                             '<script src="assets/js/jquery.backstretch.min.js"></script>']
    expected_unsafe_scripts = ['<script src="assets/js/wow.min.js"></script>',
                               '<script src="assets/js/scripts.js"></script>']

    if len(actual_safe_scripts) != len(expected_safe_scripts) \
            or len(actual_unsafe_scripts) != len(expected_unsafe_scripts):
        print("length error")
        assert False
    else:
        for i, script in enumerate(actual_safe_scripts):
            if str(script) != expected_safe_scripts[i]:
                print("safe error")
                assert False
        for i, script in enumerate(actual_unsafe_scripts):
            if str(script) != expected_unsafe_scripts[i]:
                print("unsafe error")
                assert False

    assert True


test_determines_safe_tags()
test_nonce_tags_added()