# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

class Analysis:

    def __init__(self, path, html, data_path, scripts):
        self.path = path
        self.html = html
        self.data_path = data_path
        self.scripts = []


def read_response():
    response = open(self.html)
    script = None

    for line in response:
        line.strip
        if line.startswith("<script"):
            script = line
        if script is not None and !line.startswith("</script>"):
            script += line
        if line.startswith("</script>"):
            script += line
            self.scripts.append(script)
            script = None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
