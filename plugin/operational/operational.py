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

sys.path.append(util.root_dir())


def response(flow: http.HTTPFlow):
    """
    Run automatically by mitmproxy on responses during operational phase
    :param flow:  active http flow
    :return: -
    """

    if util.check_content_type(flow):
        operation = Operational(flow, None)
        # change the response text to the one with nonce
        flow.response.text = operation.add_nonce_to_html()
        # update the CSP header of the response
        flow.response.headers["Content-Security-Policy"] = "script-src 'nonce-" + operation.get_nonce() + \
            "'; report-uri https://51f4b3cde163f2b4c157f695e578432e.report-uri.com/r/d/csp/reportOnly;"


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
        self._scripts = [[], [], []]  # Safe Script Tags = [0] Unsafe Script Tags = [1] Data scripts = [2]
        # save the flow to disk, and store its filepath
        self.set_path(util.to_disk(flow, filepath, self._file_name))
        self.operate()

    def operate(self):
        """
        Method to call the appropriate methods required to perform the operational phase
        """
        self.generate_nonce()
        self.retrieve_safe_tags()
        self.determine_safe_tags()
        # Analysis(self.get_path())

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
        # if there is a data file, get all the scripts in the data file
        if os.path.isfile(root_path):
            scripts = util.get_scripts(root_path)
            if scripts:
                # for each script in the data file, add is to the data script variable
                for script in scripts:
                    self._scripts[2].append(script)

    def determine_safe_tags(self):
        """
        Determine which script tags are safe and unsafe in the HTML
        """
        # get the file which the HTML is stored in
        root_path = os.path.join(self._path, self._file_name)
        if os.path.isfile(root_path):
            # get all the scripts which are in the html file
            scripts = util.get_scripts(root_path)
            for script in scripts:
                str_script = str(script).replace("\n", ' ')
                if str_script in str(self._scripts[2]):
                    # Safe Scripts
                    self._scripts[0].append(script)
                # otherwise, the script is unsafe and add it to the unsafe list
                else:
                    # Unsafe scripts
                    self._scripts[1].append(script)

    def add_nonce_to_html(self):
        """
        Add the nonce tags to each safe script tag
        :param self:
        :return: the html with the added nonce tags
        """
        original_html = self._response.get_response_content()

        # use bs4 for get all the scripts in the html response
        final_html = bs4.BeautifulSoup(original_html, 'html.parser')
        scripts = final_html.findAll('script')

        # for each script, if its a safe script, add a nonce to it
        for script in scripts:
            str_script = str(script).replace("\n", ' ')
            if str_script in str(self._scripts[2]):
                script.attrs['nonce'] = self._nonce

        # if there are any unsafe scripts in the html content, create a new script to generate browser warning
        if len(self._scripts[1]) != 0:
            # create the new script tag, and add the nonce and body to it
            new_script = final_html.new_tag('script')
            new_script.attrs['nonce'] = self._nonce
            new_script.string = "alert('Unsafe Script(s) detected');"
            # add the script tag to the html
            final_html.html.body.append(new_script)

        return str(final_html)
