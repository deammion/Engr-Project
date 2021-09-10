
class DataNode:

    def __init__(self, s, f, h):
        """
            Runs analysis object
            """
        self.script = s
        self.frequency = f
        self.htmls_checked = h
        self.probability = round((f/h) * 100, 2)

    def get_script(self):
        return self.script

    def get_frequency(self):
        return self.frequency

    def get_probability(self):
        return self.probability

    def set_frequency(self, f):
        self.frequency = f
        self.probability = round((f/self.htmls_checked) * 100, 2)

    def set_htmls_checked(self, h):
        self.htmls_checked = h
        self.probability = round((self.frequency / h) * 100, 2)

    def to_string(self):
        return self.script + " Frequency: " + str(self.frequency) \
                + " Probability: " + str(self.probability) + "%" + "\n"
        # return "==============================" + "\n" + self.script + "\n" + " Frequency: " + str(self.frequency) \
        #        + "\n" + " Probability: " + str(self.probability) + "%" + "\n"
