""" Module to handle command line """

import argparse
import os


class InputArgument:
    """ Handle the arguments from the terminal """
    def __init__(self) -> None:
        pass

    def is_valid_argument(self, argument: str) -> bool:
        """ Check if the argument is a valid according to specifications """
        if not os.path.abspath(argument):
            raise ValueError(f'{argument} must be an absolute path')
        if not os.path.isfile(argument):
            raise ValueError(f'{argument} does not contain a file')
        if not self.is_valid_extension(argument):
            raise ValueError(f'{argument} has the wrong extension')
        return True

    @staticmethod
    def is_valid_extension(file_path) -> bool:
        """ File extension in the path  must be .txt """
        if file_path.lower().endswith('.txt'):
            return True
        False

    @staticmethod
    def parse_arguments() -> str:
        """ Return the file path from the incoming input arguments """
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


if __name__ == "__main__":
    pass
