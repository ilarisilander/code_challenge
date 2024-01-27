""" Module to count how many times the file name occurs in it's own file """

from CommandLine import InputArgument
from Files import TextFile


def main():
    input_argument = InputArgument()
    parsed_args = input_argument.parse_arguments()
    if input_argument.is_valid_argument(parsed_args):
        text_file = TextFile(parsed_args)
        file_name = text_file.get_name_from_file_path()
        text_file.set_name(file_name)
        text_file.read_content()
        print(text_file.name)


if __name__ == "__main__":
    main()
