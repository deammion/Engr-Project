from analysis.analysis import Analysis
from operational.operational import Monitor
from utilities.util import print_header


class Instance:
    def __init__(self, phase=0):
        self._phase = phase
        self._samples = None
        self._whitelist = None
        self._blacklist = None
        self._watching = None

    def get_phase(self):
        return self._phase

    def set_phase(self, x):
        self._phase = x

    def collect(self):
        """
        Collect Samples
        Log html from visited sites and write to a file
        :return: Path of directory for analysis
        """
        try:
            print_header("STARTING COLLECTION")
            self.set_phase(self._phase + 1)
        except FileNotFoundError as e:
            print("Error collating samples ", e)

    def operate(self):
        """
        Create watcher
        Monitor traffic, identify scripts in responses, check against whitelist, block unsafe scripts & create
        report uri & browser popup, add nonce to safe scripts
        :return:
        """
        Monitor(self._whitelist, self._blacklist)
        print_header("STARTING OPERATION")
        pass


def load(self, loader):
    """
    On script load, run in phase.
    :param self:
    :param loader:
    :return:
    """
    print_header("TESTING")
    program = Instance()

    try:
        phase = program.get_phase()
        if phase == 0:
            program.collect()
        elif phase == 1:
            program.operate()
    except IOError as e:
        print("Error reading phase in main ", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load(1, 2)
