""" Module to count how many times the file name occurs in it's own file """

import os
import argparse


class TextFile:
    """ Perform operations on the text file itself  """
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = ""

    def read_content(self) -> list:
        """ Create a list from each word in a text file 
        
        Return: list
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
            #print(content)

    def extract_name_from_path(self) -> str:
        """ Remove prefix and path
        
        Return: str: file name
        """
        return file_name
    
    def set_name(self, name):
        self.name = name


class InputArguments:
    """ Handle the arguments from the terminal """
    def __init__(self) -> None:
        self.input_argument = ""

    def parse_arguments():
        arg_parser = argparse.ArgumentParser(description='WordCounter is an application that count the words in a text file')
        arg_parser.add_argument('--file_path', type=str, help='Path to file', required=True)
        arguments = arg_parser.parse_args()
        return arguments
    
    def set_input_argument(self, input_argument):
        if os.path.isfile(input_argument):
            self.input_argument = input_argument
        
    def get_input_argument(self):
        return self.input_argument
    
    def validate_arguments(self, arguments):
        # Check if arguments contains only one argument
        if self.contains_one_argument(arguments)
        # Check if argument is a valid path

        # Check if argument is a file
        pass

    @staticmethod
    def contains_one_argument(arguments) -> bool:
        """ Argument must only contain one argument"""
        pass

class Word:
    """ Search for the specific word inside the text file """
    def __init__(self) -> None:
        pass

    def find_word(self):
        pass


def main():
    input_arguments = InputArguments()
    parsed_args = input_arguments.parse_arguments()
    text_file = TextFile(parsed_args.file_path)
    text_file.read_content()


if __name__ == "__main__":
    main()
