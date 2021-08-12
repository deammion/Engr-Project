"""
Perform blocking and reporting on scripts, add nonces to , and allow, safe scripts
"""

from __future__ import absolute_import
import secrets
import time
import os
import sys
from mitmproxy import http
import bs4

from utilities import util
from utilities.util import root_dir
from analysis.analysis import Analysis

sys.path.append(root_dir())


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses during operational phase
    :param flow:  active http flow
    :return: -
    """
    print("response")

    if util.correct_filetype(flow):
        #flow.response.text = "<h1>test</h1>"
        #flow.response.headers["Content-Security-Policy"] = "script-src 'nonce-{random}'"
        Monitor(flow)

class Monitor:
    """
    Object watches a stream
    """
    def __init__(self, flow):
        self._sample = None
        self._flow = flow
        self._path = None
        self._nonce = None
        self._file_name = str(time.time())
        self.set_path(util.to_disk(self._flow, self._file_name))
        self._scripts = [[]] * 4  # Safe Script Tags = [0] Unsafe Script Tags = [1] Data scripts = [2]
        self.retrieve_safe_tags()
        self.determine_safe_tags()
        Analysis(self.get_path())

    def get_path(self):
        """
        Get the path of the object
        :return: object path
        """
        return self._path

    def set_path(self, path):
        """
        Set the path of the object
        :param path: new path
        :return: -
        """
        self._path = path

    def get_filename(self):
        """
        Get the name of the file from the object
        :return: file name
        """
        return self._file_name

    def generate_nonce(self):
        """
        Generate nonce using secrets. Secrets is a
        CSPRNG. Creates a 256 bit (32 byte)token
        encoded in Base64
        Returns: Base64 encoded nonce.

        """
        self._nonce = secrets.token_urlsafe(32)
        return self._nonce

    def retrieve_safe_tags(self):
        """
        Retrieve the script tags which are deemed as safe from the data.txt file
        """
        root_path = os.path.join(self._path, "data.txt")
        if os.path.isfile(root_path):
            file = open(root_path, "r")
            file_data = file.read()
            soup = bs4.BeautifulSoup(file_data, 'html.parser')
            scripts = soup.find_all('script')
            if scripts:
                for script in scripts:
                    self._scripts[2].append(script)

    def determine_safe_tags(self):
        """
        Determine which script tags are safe and unsafe in the HTML
        """
        root_path = os.path.join(self._path, self._file_name)
        if os.path.isfile(root_path):
            file = open(root_path, "r")
            file_data = file.read()
            soup = bs4.BeautifulSoup(file_data, 'html.parser')
            scripts = soup.find_all('script')
            for script in scripts:
                if script in self._scripts[2]:
                    # Safe Scripts
                    self._scripts[1].append(script)
                else:
                    # Unsafe scripts
                    self._scripts[0].append(script)

    def add_nonce_to_html(self):
        """
        Add the nonce tags to each safe script tag
        :param self:
        :return: the html with the added nonce tags
        """
        original_html = self._flow.response.text

        final_html = bs4.BeautifulSoup(original_html, 'html.parser')
        scripts = final_html.findAll('script')
        for script in scripts:
            if script in self._scripts[2]:
                script.attrs['nonce'] = self._nonce

        return final_html

    def report(self, flow):
        """
        Created a report method which goes through a list a unsafe script tags and if the tag is unsafe it will be sent to report uri.
        :return: -
        """
        url = flow.request.pretty_url
        csp_report_uri = '<https://ae939929c62b2dec1ba2ddee3176d018.report-uri.com/r/d/csp/reportOnly>'
        browser_warning = "<script> window.alert(\"Unsafe Script(s) detected\");</script>"
        if len(self._scripts[1]) == 0:
            print("List is empty")
        else:
            for script in self._scripts[1]:
                if script in url:
                    script = csp_report_uri
                    print(script + "This is an unsafe script")
            with open(self._file_name, "r") as f:
                content = f.readlines()
                content.insert(len(content) - 4, browser_warning)
                to_write = ""
                f.close()
            with open(self._file_name, "w") as f:
                for line in content:
                    to_write = to_write + line
                print(to_write)
                f.write(to_write)
