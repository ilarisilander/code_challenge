""" Module to count how many times the file name occurs in it's own file """

import os
import argparse
from CustomExceptions import InvalidExtentionError


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


class TerminalArgument:
    """ Handle the arguments from the terminal """
    def __init__(self) -> None:
        pass

    def is_valid_argument(self, argument: str) -> bool:
        """ Check if the argument is a valid according to specifications """
        if not os.path.exists(argument):
            raise FileNotFoundError(f'{argument} does not exist')
        if not os.path.abspath(argument):
            raise ValueError(f'{argument} must be an absolute path')
        if not os.path.isfile(argument):
            raise ValueError(f'{argument} does not contain a file')
        if not self.is_valid_extension(argument):
            raise InvalidExtentionError(f'{argument} has the wrong extension')
        return True

    @staticmethod
    def is_valid_extension(file_path) -> bool:
        """ File extension must be .txt """
        if file_path.lower().endswith('.txt'):
            return True
        False

    @staticmethod
    def parse_arguments() -> str:
        """ Retrieve the file path from the incoming terminal arguments """
        arg_parser = argparse.ArgumentParser(
            description='An application to count the specific word in a file'
        )

        arg_parser.add_argument(
            '--file_path',
            type=str,
            help='Path to file',
            required=True
        )

        argument = arg_parser.parse_args()
        return argument.file_path


def main():
    terminal_argument = TerminalArgument()
    parsed_args = terminal_argument.parse_arguments()
    if terminal_argument.is_valid_argument(parsed_args):
        text_file = TextFile(parsed_args)
        file_name = text_file.get_name_from_file_path()
        text_file.set_name(file_name)
        text_file.read_content()


if __name__ == "__main__":
    main()
