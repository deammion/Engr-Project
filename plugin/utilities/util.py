"""
Utility methods used across modules
"""
from __future__ import absolute_import
from __future__ import division
import os
import bs4
from mitmproxy import io, http
from mitmproxy.exceptions import FlowReadException


def root_dir():
    """
    Get the root directory of the program
    :return: path to plugin directory
    """
    return os.path.dirname(os.path.dirname(__file__))


def print_header(header: str):
    """
    Print a heading
    :param header: content to print centered
    :return:
    """
    center = 20 - int(len(header) / 2)
    print("=" * center, header, "=" * center)


def to_disk(flow, filepath, filename):
    """
        Saves information to a file on the disk
        :param flow: object
        :param filepath: file path of the file
        :param filename name of file
        :return: new root path
        """
    data = flow.request.pretty_url.split("/")
    data = data[2:]
    if filepath is None:
        root_path = os.getcwd()
    else:
        root_path = filepath
    for folder in data:
        root_path = os.path.join(root_path, folder)
        if not os.path.exists(root_path):
            os.mkdir(root_path)
    file_path = os.path.join(root_path, filename)
    file = open(file_path, "w")
    file.write(flow.response.text + "\n")
    file.close()
    return root_path


def get_scripts(filename):
    """
    Reads the HTML from a file and gets a list of all the script tags in the file
    :return: a list of all the script tags in the file
    """
    file = open(filename, "r")
    file_data = file.read()
    # Scan read in file using html parser
    soup = bs4.BeautifulSoup(file_data, 'html.parser')
    # Extract script tags from html
    scripts = soup.find_all('script')
    file.close()
    return scripts


def check_content_type(flow):
    """
    Check content type of response HTTP
    :param flow: http flow for proxy
    :return: Boolean true is content type is text/html
    """
    headers = flow.response.headers.items()
    for key, value in headers:
        if key.upper() == 'CONTENT-TYPE' and "text/html;" in value:
            return True
    return None


def load_flow(filename):
    """
    USED FOR COLLECTION AND OPERATION PHASE TESTING

    Create a method to load a flow so the operation class can be created
    Code taken directly from https://docs.mitmproxy.org/stable/addons-examples/
    :param filename: file name of the file to load
    :return: http flow for proxy
    """
    with open(filename, "rb") as logfile:
        f_reader = io.FlowReader(logfile)
        try:
            for flow in f_reader.stream():
                if isinstance(flow, http.HTTPFlow):
                    return flow
        except FlowReadException as exception:
            print(f"Flow file corrupted: {exception}")
    return None
