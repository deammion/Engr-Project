"""
Test analysis phase
"""
from __future__ import absolute_import
import difflib
import os

from analysis.analysis import Analysis
from utilities.util import root_dir


def test_match():
    """
    Test output from analysis matches expected output for a given sample output delta difference
    :return: -
    """
    Analysis(root_dir() + '/data/samples/dev.unshielded.red')

    expected = open(os.path.join(root_dir(), 'data/outputs/expected/analysis.txt'))
    actual = open(os.path.join(root_dir(), 'data/samples/dev.unshielded.red/data.txt'))

    diff = difflib.ndiff(expected.readlines(), actual.readlines())

    delta = ''.join(x[2:] for x in diff if x.startswith('- '))

    if not delta:
        assert True
    else:
        assert False


if __name__ == '__main__':
    test_match()


def test_no_correct_files():
    """
        Test for correct output with files without script tags
        :return: -
    """
    print("HELLO")
    Analysis(root_dir() + '/data/samples/no_script_tags_sample')

    print("HIII")
    expected = open(os.path.join(root_dir(), 'data/outputs/expected/script_analysis.txt'))
    print("MORNING")
    actual = open(os.path.join(root_dir(), 'data/samples/no_script_tags_sample/data.txt'))

    diff = difflib.ndiff(expected.readlines(), actual.readlines())

    delta = ''.join(x[2:] for x in diff if x.startswith('- '))

    if not delta:
        print("123")
        assert True
    else:
        print("!!!!!!")
        assert False


if __name__ == '__main__':
    test_no_correct_files()
