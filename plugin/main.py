from operational.operational import Monitor
from utilities.util import print_header, print_sub

"""
New instance of the Red Shield Program
"""

class Instance:
    """
    Creates a new instance of the program
    """
    def __init__(self, phase=0):
        """
        Initialiases the current instance
        :param self:
        :param phase:
        :return:
        """
        self._phase = phase
        self._samples = None
        self._whitelist = None
        self._blacklist = None
        self._watching = None

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
        :param x:
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
            print_sub("Phase: " + str(self._phase))
            print_header("STARTING COLLECTION")
            input(" PRESS ENTER TO CONTINUE TO NEXT PHASE ")

            self.set_phase(self._phase + 1)
            print("\n\n")
            print_sub("Phase: " + str(self._phase))
            run(self)
        except FileNotFoundError as error:
            print("Error collating samples ", error)

    def operate(self):
        """
        Create watcher
        Monitor traffic, identify scripts in responses, check against whitelist, block unsafe scripts & create
        report uri & browser popup, add nonce to safe scripts
        :param self:
        :return:
        """
        print_header("STARTING OPERATION")
        input(" PRESS ENTER TO CONTINUE TO NEXT PHASE ")

        self.set_phase(self._phase + 1)
        print("\n\n")


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
    load(1, 2)
