""" Module to count how many times the file name occurs in it's own file """

import sys
import logging

from CommandLine import InputArgument
from Files import TextFile


def main():
    input_argument = InputArgument()
    parsed_args = input_argument.parse_arguments()

    try:
        valid_argument = input_argument.is_valid_argument(parsed_args)
    except ValueError as ve:
        logging.error(f'Error: {ve}')
        sys.exit(1)
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        sys.exit(1)

    if valid_argument:
        text_file = TextFile(parsed_args)
        file_name = text_file.get_name_from_file_path()
        text_file.set_name(file_name)
        content_list = text_file.file_content_to_list()
        word_counter = text_file.count_words_in_list(content_list)
        print(word_counter)


if __name__ == "__main__":
    main()
