"""
New instance of the Red Shield Program
"""
from __future__ import absolute_import

import sys

from utilities.util import print_header


class Instance:
    """
    Creates a new instance of the program
    """

    def __init__(self, phase=False):
        """
        Initialises the current instance
        :param self:
        :param phase:
        :return:
        """
        self._phase = phase
        self._samples = None
        self._whitelist = None
        self._blacklist = None
        self._watching = None

    def progression(self, stage):
        """
        Progress Phase on User Input
        -- Here for Demonstration
        :param stage: stage to print in heading
        :return: -
        """
        print_header("Starting " + stage)
        print(" Press enter to continue to the next phase ")
        sys.stdin.readline()
        self.set_phase(self._phase + 1)
        print("\n\n")

    def get_phase(self):
        """
        Returns the phase the current instance is in
        :param self:
        :return: the current phase
        """
        return self._phase

    def set_phase(self, new_phase):
        """
        Sets the phase for the current instance
        :param self:
        :param new_phase:
        :return:
        """
        self._phase = new_phase

    def collect(self):
        """
        Collect Samples
        Log html from visited sites and write to a file
        :param self:
        :return: Path of directory for analysis
        """
        try:
            self.progression("Collection")
            run(self)
        except FileNotFoundError as error:
            print("Error collating samples ", error)

    def operate(self):
        """
        Create watcher
        Monitor traffic, identify scripts in responses, check against whitelist, block unsafe
        scripts & create report uri & browser popup, add nonce to safe scripts
        :param self:
        :return:
        """
        self.progression("Operation")


def load():
    """
    On script load, run in phase.
    :return:
    """
    program = Instance()

    run(program)


def run(program):
    """
    Returns the phase the current instance is in
    :param program:
    :return:
    """
    try:
        phase = program.get_phase()
        if phase == 0:
            program.collect()
        elif phase == 1:
            program.operate()
    except IOError as error:
        print("Error reading phase in main ", error)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load()
