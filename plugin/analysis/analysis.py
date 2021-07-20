# This is a sample Python script.
import re


class Analysis:

    """
    Corresponds to collection object
    """

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
