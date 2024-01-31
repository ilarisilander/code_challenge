""" Module to handle the users input arguments from the command line """

import argparse
import os


class InputArgument:
    """ Handle the arguments from the terminal """

    def is_valid_argument(self, argument: str) -> bool:
        """ Check if the argument is a valid according to specifications """
        if not os.path.isfile(argument):
            raise ValueError(f'{argument} path is invalid')
        if not self.is_valid_extension(argument):
            raise ValueError(f'{argument} has the wrong extension')
        if not self.file_has_no_spaces(argument):
            raise ValueError(f'{argument} has spaces in file name')
        return True

    @staticmethod
    def is_valid_extension(file_path: str) -> bool:
        """ File extension in the path must be .txt """
        if file_path.endswith('.txt'):
            return True
        False

    @staticmethod
    def file_has_no_spaces(file_path):
        """ Check for spaces in the file name """
        file_name = os.path.basename(file_path)
        for char in file_name:
            if char.isspace():
                return False
        return True

    @staticmethod
    def parse_arguments() -> str:
        """ Return the file path from the incoming input arguments """
        arg_parser = argparse.ArgumentParser(
            description='''Add a path to a .txt file as an argument after --file_path.
            A valid command could look like this: python WordCounter.py --file_path c:/temp/word_file.txt.'''
        )

        arg_parser.add_argument(
            '--file_path',
            type=str,
            help='Path to file',
            required=True
        )

        argument = arg_parser.parse_args()
        return argument.file_path.lower()


if __name__ == '__main__':
    # I leave this if statement because it will prevent
    # accidental code executions when importing this module.
    pass
