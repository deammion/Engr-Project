import re
import os


class Analysis:
    """
    Corresponds to collection object
    """

    def __init__(self, html):
        self.html = html
        self.scripts = []
        self.read_directory()

    def read_directory(self):
        """
                Read all response text files in the given directory
                :return:
                """
        os.chdir(self.html)
        for file in os.listdir():
            if file.endswith("response.txt"):
                to_read = f"{os.getcwd()}/{file}"
                get_tags(self, to_read)
        for x in self.scripts:
            print(x)


def get_tags(self, file):
    """
        Identify & strip tags from response files
        :return:
        """
    print("Reading File: " + file)
    response = open(file)
    text = response.read()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    scripts = re.findall('(<script.+?</script>)', text.strip())
    if scripts:
        for x in scripts:
            self.scripts.append(x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
            Run analysis on all files in the sample data directory
            :return:
            """
    Analysis('../data/samples/dev.unshielded.red')
