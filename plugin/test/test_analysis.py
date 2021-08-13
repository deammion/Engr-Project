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
    actual = open(os.path.join(root_dir(), 'data/outputs/actual/analysis.txt'))

    diff = difflib.ndiff(expected.readlines(), actual.readlines())

    delta = ''.join(x[2:] for x in diff if x.startswith('- '))
    print("DELTA:", delta)

if __name__ == '__main__':
    test_match()
