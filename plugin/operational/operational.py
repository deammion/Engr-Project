"""
Perform blocking and reporting on scripts, add nonces to , and allow, safe scripts
"""

from __future__ import absolute_import
import re
import secrets
import time
import os
import sys
from mitmproxy import http

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
        self._scripts = [[]]  # Whitelist [0] blacklist [1]   operation scripts[2] Data scripts = [3]
        self.calculate_safe_tags()
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

    def calculate_safe_tags(self):
        """
        Identify safe tags from response file
        :return:
        """
        os.chdir(self._path)
        for file in os.listdir():
            if file.endswith("data.txt") or self._file_name:
                file = open(file)
                text = file.read()
                text = text.replace('\n', '')
                text = text.replace('\t', '')
                scripts = re.findall('(<script.+?</script>)', text.strip())
                if scripts:
                    if file.name == "data.txt":
                        for script in scripts:
                            self._scripts[2].append(script)
                    elif file.name == self._file_name:
                        for script in scripts:
                            self._scripts[3].append(script)
        for script in self._scripts[3]:
            if script in self._scripts[2]:
                # Safe Scripts
                self._scripts[0].append(script)
            else:
                # Unsafe scripts
                self._scripts[1].append(script)
