# This is a sample Python script.
import re


class Analysis:

    def __init__(self, html):
        # self.path = path
        self.html = html
        # self.data_path = data_path
        self.scripts = []
        self.get_tags()

    def get_tags(self):
        response = open(self.html)
        text = response.read()
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        scripts = re.findall('(<script.+?</script>)', text.strip())
        if scripts:
            self.scripts = scripts
            for x in self.scripts:
                print(x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = Analysis("samples/samples/dev.unshielded.red/1-response.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
