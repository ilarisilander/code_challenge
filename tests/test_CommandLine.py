""" Test cases for the CommandLine module """

import unittest
from libraries.CommandLine import InputArgument
from unittest.mock import patch, MagicMock


class TestInputArgument(unittest.TestCase):

    def setUp(self):
        self.input_argument = InputArgument()

    # valid_extension function

    def test_valid_extension_return_true(self):
        test_input = 'c:/dummy_path/example.txt'
        bool_result = self.input_argument.is_valid_extension(test_input)
        self.assertTrue(bool_result)

    def test_valid_extension_capital_letters_return_true(self):
        test_input = 'c:/dummy_path/EXAMPLE.TXT'
        bool_result = self.input_argument.is_valid_extension(test_input)
        self.assertTrue(bool_result)

    def test_valid_extension_return_false(self):
        test_input = 'c:/dummy_path/example.jpeg'
        bool_result = self.input_argument.is_valid_extension(test_input)
        self.assertFalse(bool_result)

    @patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(file_path='c:/example/test_file.txt')
        result = InputArgument.parse_arguments()
        self.assertEqual(result, 'c:/example/test_file.txt')
