"""
Perform blocking and reporting on scripts, add nonces to, and allow, safe scripts
"""

from __future__ import absolute_import
import secrets
import os
import sys
from mitmproxy import http
import bs4

from utilities import util
from utilities.response import Response
from utilities.request import Request
from analysis.analysis import Analysis

sys.path.append(util.root_dir())


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses during operational phase
    :param flow:  active http flow
    :return: -
    """

    if util.check_content_type(flow):
        operation = Operational(flow)
        flow.response.text = operation.add_nonce_to_html()
        flow.response.headers["Content-Security-Policy"] = "script-src 'nonce-{" + operation.get_nonce() + "}';" \
            "  report-uri https://ae939929c62b2dec1ba2ddee3176d018.report-uri.com/r/d/csp/reportOnly"


class Operational:
    """
    Method to initialize an operation object
    """
    def __init__(self, flow, filepath):
        self._request = Request(flow)
        self._response = Response(flow)
        self._path = None
        self._nonce = None
        self._file_name = self._response.get_time()
        self._scripts = [[], [], []] * 4  # Safe Script Tags = [0] Unsafe Script Tags = [1] Data scripts = [2]
        self.set_path(util.to_disk(flow, filepath, self._file_name))
        self.operate()

    def operate(self):
        """
        Method to call the appropriate methods required to perform the operational phase
        """
        self.generate_nonce()
        self.retrieve_safe_tags()
        self.determine_safe_tags()
        Analysis(self.get_path())

    def get_path(self):
        """
        Get the path of the object
        :return: object path
        """
        return self._path

    def get_scripts(self):
        """
        Get the scripts of the object
        :return: object scripts
        """
        return self._scripts

    def get_nonce(self):
        """
        Get the nonce of the object
        :return: object nonce
        """
        return self._nonce

    def set_path(self, path):
        """
        Set the path of the object
        :param path: new path
        :return: -
        """
        self._path = path

    def set_nonce(self, nonce):
        """
        Set the nonce of the object
        This method is only used for testing purposes
        :param nonce: new nonce
        """
        self._nonce = nonce

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
            scripts = util.get_scripts(root_path)
            if scripts:
                for script in scripts:
                    self._scripts[2].append(script)

    def determine_safe_tags(self):
        """
        Determine which script tags are safe and unsafe in the HTML
        """
        root_path = os.path.join(self._path, self._file_name)
        if os.path.isfile(root_path):
            scripts = util.get_scripts(root_path)
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
        original_html = self._response.get_response_content()

        final_html = bs4.BeautifulSoup(original_html, 'html.parser')
        scripts = final_html.findAll('script')
        for script in scripts:
            if script in self._scripts[2]:
                script.attrs['nonce'] = self._nonce

        return str(final_html)

    def report(self):
        """
        Created a report method which goes through a list a unsafe script tags and if the tag is unsafe it will be sent to report uri.
        :return: -
        """
        url = self._request.get_url()
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
