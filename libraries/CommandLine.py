""" Module to handle command line """

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
        return True

    @staticmethod
    def is_valid_extension(file_path: str) -> bool:
        """ File extension in the path must be .txt """
        if file_path.endswith('.txt'):
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
        return argument.file_path.lower()


if __name__ == '__main__':
    # I leave this if statement because it will prevent
    # accidental code executions when importing this module.
    pass
