"""
Test Operation Phase
"""

from __future__ import absolute_import
import os


from operational.operational import Operational
from utilities import util
from utilities.util import root_dir


def test_nonce_tags_added():
    """
    Test that checks that nonce tags are correctly added to all safe script tags.
    """
    flow = util.load_flow(root_dir() + '/flowInfo.txt')
    operational = Operational(flow, root_dir() + '/data/outputs/actual/testingNonceTags')
    operational.set_nonce("THIS_IS_NONCE")

    # write the created output to a file for later comparison
    file = open(root_dir() + '/data/outputs/actual/operational.txt', "w")
    file.write(operational.add_nonce_to_html())
    file.close()

    expected_script = util.get_scripts(os.path.join(root_dir(), 'data/outputs/expected/operational.txt'))
    actual_script = util.get_scripts(os.path.join(root_dir(), 'data/outputs/actual/operational.txt'))

    if len(expected_script) != len(actual_script):
        assert False
    else:
        for i, script in enumerate(actual_script):
            if expected_script[i] != script:
                assert False

    assert True


def test_determines_safe_tags():
    """
    Test that checks that the program correctly determines which script tags are safe and unsafe
    """
    # Create the flow and operational class
    flow = util.load_flow(root_dir() + '/flowInfo.txt')
    operational = Operational(flow, root_dir() + '/data/outputs/actual/operationalOutput')

    # Get the operational script tags
    actual_safe_scripts = operational.get_scripts()[0]
    actual_unsafe_scripts = operational.get_scripts()[1]

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

    # compare the script tags to check that they are the same
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


def test_determine_data_tags():
    """
    Test that checks that the program correctly reads script tags from the data file
    """
    # Create the flow and operational class
    flow = util.load_flow(root_dir() + '/blankFlow.txt')
    operational = Operational(flow, root_dir() + '/data/outputs/actual/operationalOutput')

    # Get the operational script tags
    actual_data_scripts = operational.get_scripts()[2]

    expected_data_scripts = ['<script src="script1"></script>',
                             '<script src="script2"></script>']

    # compare the script tags to check that they are the same
    if len(actual_data_scripts) != len(expected_data_scripts):
        print("Length error")
        assert False
    else:
        for i, script in enumerate(actual_data_scripts):
            if str(script) != expected_data_scripts[i]:
                print("Safe error")
                assert False
    assert True


test_determines_safe_tags()
test_nonce_tags_added()
test_determine_data_tags()
