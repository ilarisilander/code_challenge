""" Module to handle files """

import os
import re


class TextFile:
    """ Perform operations on the text file itself """
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = ""

    def file_content_to_list(self) -> list:
        """ Create a list from each word in a text file """
        with open(self.path, 'r', encoding='utf-8') as file:
            content = file.read()
            word_list = re.split(r'\s+', content)  # remove spaces and new line
            return word_list

    def get_name_from_file_path(self):
        """ Remove prefix and path """
        file = os.path.basename(self.path)
        file_name = os.path.splitext(file)[0]
        return file_name

    def set_name(self, name):
        self.name = name

    def count_words_in_list(self, word_list: list) -> int:
        """ Count how many times the file name appears in the word list """
        counter = 0
        for word in word_list:
            if self.name.lower() in word.lower():
                counter += 1
        return counter

    def print_word_count(self, counter: int):
        print(f'The word "{self.name}" appeared {counter} times')


if __name__ == '__main__':
    # I leave this if statement because it will prevent
    # accidental code executions when importing this module.
    pass
