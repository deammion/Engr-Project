"""
Utility methods used across modules
"""
from __future__ import absolute_import
from __future__ import division
import hashlib
import os
import bs4


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


def sha256sum(filename):
    """
    Hash file contents
    :param filename:  name of file to hash
    :return: sha256 hash of file
    """
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


def correct_filetype(flow):
    """
    Check file extension matches allowed types
    :param flow: http flow to check file extensions upon
    :return: True if extension matches allowed type
    """
    url = flow.request.pretty_url
    if not (url.endswith(".css") or
            url.endswith(".jpg") or
            url.endswith(".png") or
            url.endswith(".js") or
            url.__contains__("www.gstatic.com")):
        return True
    return False


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


def dump_output(content, subdir, name):
    """
    Dump an array to a file at subdir from root with name name
    :param content: Content to print
    :param subdir: Subdir from root directory (plugin)
    :param name: file name
    :return:
    """
    file_path = os.path.join(subdir, name)
    with open(os.path.join(root_dir(), file_path), "w") as output:
        output.writelines(str(content[i]) + "\n" for i in range(len(content)))
    output.close()


def get_scripts(filename):
    """
    Reads the HTML from a file and gets a list of all the script tags in the file
    :return: a list of all the script tags in the file
    """
    file = open(filename, "r")
    file_data = file.read()
    soup = bs4.BeautifulSoup(file_data, 'html.parser')
    scripts = soup.find_all('script')
    file.close()
    return scripts


def check_content_type(flow):
    """
    Check content type of response HTTP
    :param flow:
    :return: Boolean true is content type is text/html
    """
    headers = flow.response.headers.items()
    for key, value in headers:
        if key.upper() == 'CONTENT-TYPE' and "text/html;" in value:
            return True
    return None
