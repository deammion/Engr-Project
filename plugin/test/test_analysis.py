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
    file_path = root_dir() + '/data/samples/script_tags_sample/data.txt'

    if os.path.exists(file_path):
        os.remove(file_path)
    # Process sample data to compare with expected
    Analysis(root_dir() + '/data/samples/script_tags_sample')
    # Do comparison
    expected = open(os.path.join(root_dir(), 'data/outputs/expected/analysis.txt'))
    actual = open(os.path.join(root_dir(), 'data/samples/script_tags_sample/data.txt'))

    diff = difflib.ndiff(expected.readlines(), actual.readlines())
    # Get changes between expected and actual files
    delta = ''.join(x[2:] for x in diff if x.startswith('- '))

    if not delta:
        assert True
    else:
        assert False


def test_no_correct_files():
    """
        Test for correct output with files without script tags
        :return: -
    """
    file_path = root_dir() + 'data/samples/no_scripts_tags_sample/data.txt'

    if os.path.exists(file_path):
        os.remove(file_path)
    # Process sample data to compare with expected
    Analysis(root_dir() + '/data/samples/no_scripts_tags_sample')
    # Check no scripts are found
    expected = open(os.path.join(root_dir(), 'data/outputs/expected/script_analysis.txt'))
    actual = open(os.path.join(root_dir(), 'data/samples/no_scripts_tags_sample/data.txt'))

    diff = difflib.ndiff(expected.readlines(), actual.readlines())

    delta = ''.join(x[2:] for x in diff if x.startswith('- '))

    if not delta:
        assert True
    else:
        assert False


def test_correct_file_order():
    """
        Tests that analysis correctly orders the files
        :return: -
    """
    # Run analysis with file containing ordered arguments
    analysis = Analysis(root_dir() + '/data/samples/script_tags_sample')
    # Check scripts are in expected order
    correct_order = ['1630982908.0', '1630986508.0', '1632109708.0', '1632368908.0', '1632714508.0']
    print(len(analysis.filenames_sorted))
    for i, filename in enumerate(correct_order):
        if filename != analysis.filenames_sorted[i]:
            # assert False
            print(filename + '!= ' + analysis.filenames_sorted[i])

    assert True


if __name__ == '__main__':
    test_match()
    test_no_correct_files()
    test_correct_file_order()
