import hashlib
import mmap

import os


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
    sz = 20 - int(len(header) / 2)
    print("=" * sz, header, "=" * sz)


def print_sub(sub: str):
    """
    Print a subheading
    :param sub: content to print centered
    :return: -
    """
    sz = 20 - int(len(sub) / 2)
    print(" " * sz, sub, " " * sz)


def sha256sum(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


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
