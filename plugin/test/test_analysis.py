import difflib
import filecmp
import os
from analysis.analysis import Analysis
from utilities.util import sha256sum, root_dir


def test_match():
    Analysis(root_dir() + '/data/samples/dev.unshielded.red')

    f1 = open(os.path.join(root_dir(), 'data/outputs/expected/analysis.txt'))
    f2 = open(os.path.join(root_dir(), 'data/outputs/actual/analysis.txt'))

    diff = difflib.ndiff(f1.readlines(), f2.readlines())

    delta = ''.join(x[2:] for x in diff if x.startswith('- '))
    print("DELTA:", delta)
