from operational.operational import Monitor
from utilities.util import print_header, print_sub


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
            print_sub("Phase: " + str(self._phase))
            print_header("STARTING COLLECTION")
            input(" PRESS ENTER TO CONTINUE TO NEXT PHASE ")

            self.set_phase(self._phase + 1)
            print("\n\n")
            print_sub("Phase: " + str(self._phase))
            run(self)
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
        input(" PRESS ENTER TO CONTINUE TO NEXT PHASE ")

        self.set_phase(self._phase + 1)
        print("\n\n")
        pass


def load(self, loader):
    """
    On script load, run in phase.
    :param self:
    :param loader:
    :return:
    """
    program = Instance()

    run(program)


def run(program):
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
