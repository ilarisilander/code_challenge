""" Module to handle files """

import os


class TextFile:
    """ Perform operations on the text file itself """
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = ""

    def read_content(self) -> list:
        """ Create a list from each word in a text file """
        with open(self.path, 'r') as file:
            content = file.read()
            print(content)

    def get_name_from_file_path(self):
        """ Remove prefix and path """
        file = os.path.basename(self.path)
        file_name = os.path.splitext(file)[0]
        return file_name

    def set_name(self, name):
        self.name = name


if __name__ == "__main__":
    pass
