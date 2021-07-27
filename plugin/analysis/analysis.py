import re
import os
import uuid


class Analysis:
    """
    Corresponds to collection object
    """

    def __init__(self, html):
        self.html = html
        self.scripts = []
        self.scriptToCount = {}
        self.read_directory()
        self.get_script_count()
        self.write_to_file()

    # opens all files, calls get_tags - stand in function
    # change to search for existing doc, if yes - convert to dictionary(MAP)
    def read_directory(self):
        """
                Read all response text files in the given directory
                :return:
                """
        os.chdir(self.html)
        for file in os.listdir():
            if file.endswith("response.txt"):
                read = f"{os.getcwd()}/{file}"
                self.get_tags(read)
        for x in self.scripts:
            print(x)

    # find all script tags store to array
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
        response.close()

    # count all script tags in scripts, assign to dictionary(map in java)
    def get_script_count(self):
        i = 0
        while i < len(self.scripts):
            count = self.scripts.count(self.scripts[i])
            self.scriptToCount.update({self.scripts[i]: count})
            i += 1

    def write_to_file(self):
        save_path = 'data/outputs/actual'
        file_name = str(uuid.uuid4()) + ".txt"
        dir_root = os.path.dirname(__file__) + '/../'
        file_path = os.path.join(save_path, file_name)
        with open(os.path.join(dir_root, file_path), "w") as output:
            output.writelines(key + " Frequency: " + str(self.scriptToCount[key]) + " Probability: "
                              + str(round((self.scriptToCount[key]/len(self.scripts))*100, 2))
                              + "%" + "\n" for key in self.scriptToCount)

        # f = open("whiteList.txt", "w+")
        # for key in self.scriptToCount:
        #     f.write(key + ": " + str(self.scriptToCount[key]) + "\n")
        # f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
            Run analysis on all files in the sample data directory
            :return:
            """
    Analysis('../data/samples/dev.unshielded.red')
