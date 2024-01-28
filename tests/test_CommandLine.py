""" Test cases for the CommandLine module """

import unittest
from libraries.CommandLine import InputArgument
from unittest.mock import patch, MagicMock

MODULE_PATH = 'libraries.CommandLine.'


class TestInputArgument(unittest.TestCase):

    def setUp(self):
        self.input_argument = InputArgument()
        self.dummy_path = 'c:/dummy_path/'
        self.example_txt_path = 'c:/dummy_path/example.txt'
        self.invalid_ext = 'invalid_extension.jpeg'

    def test_file_has_no_spaces_return_true(self):
        """ File name has no spaces in the name """
        input_name = 'file_name_without_spaces.txt'
        result = self.input_argument.file_has_no_spaces(input_name)
        self.assertTrue(result)

    def test_file_has_no_spaces_return_false(self):
        """ File name has spaces in the file name """
        input_name = 'file name with spaces.txt'
        result = self.input_argument.file_has_no_spaces(input_name)
        self.assertFalse(result)

    ###################
    # valid_extension #
    ###################

    def test_valid_extension_return_true(self):
        test_input = self.dummy_path + 'example.txt'
        result = self.input_argument.is_valid_extension(test_input)
        self.assertTrue(result)

    def test_valid_extension_return_false(self):
        test_input = self.dummy_path + 'example.jpeg'
        result = self.input_argument.is_valid_extension(test_input)
        self.assertFalse(result)

    @patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(file_path=self.example_txt_path)
        result = InputArgument.parse_arguments()
        self.assertEqual(result, self.example_txt_path)

    #####################
    # is_valid_argument #
    #####################

    @patch(MODULE_PATH + 'InputArgument.file_has_no_spaces')
    @patch('os.path.isfile')
    @patch(MODULE_PATH + 'InputArgument.is_valid_extension')
    def test_is_valid_argument_happy_path(self, mock_is_valid_extension,
                                          mock_isfile, mock_file_has_no_spaces):

        """ All checks should pass """

        mock_isfile.return_value = True
        mock_is_valid_extension.return_value = True
        mock_file_has_no_spaces.return_value = True

        result = self.input_argument.is_valid_argument(self.example_txt_path)

        self.assertTrue(result)
        mock_isfile.assert_called_once_with(self.example_txt_path)
        mock_is_valid_extension.assert_called_once_with(self.example_txt_path)

    @patch('os.path.isfile')
    @patch(MODULE_PATH + 'InputArgument.is_valid_extension')
    def test_is_valid_argument_not_a_file(self, mock_is_valid_extension,
                                          mock_isfile):
        """ Is file check should throw an exception """

        mock_isfile.return_value = False

        with self.assertRaises(ValueError) as context:
            self.input_argument.is_valid_argument('invalid_path.txt')

        actual = str(context.exception)
        expected = 'invalid_path.txt path is invalid'

        self.assertEqual(expected, actual)
        mock_isfile.assert_called_once_with('invalid_path.txt')
        mock_is_valid_extension.assert_not_called()

    @patch('os.path.isfile')
    @patch(MODULE_PATH + 'InputArgument.is_valid_extension')
    def test_is_valid_argument_wrong_extension(self, mock_is_valid_extension,
                                               mock_isfile):
        """ Is valid extension check should throw an exception """

        mock_isfile.return_value = True
        mock_is_valid_extension.return_value = False

        with self.assertRaises(ValueError) as context:
            self.input_argument.is_valid_argument(self.invalid_ext)

        actual = str(context.exception)
        expected = 'invalid_extension.jpeg has the wrong extension'

        self.assertEqual(expected, actual)
        mock_isfile.assert_called_once_with(self.invalid_ext)
        mock_is_valid_extension.assert_called_once_with(self.invalid_ext)

    @patch(MODULE_PATH + 'InputArgument.file_has_no_spaces')
    @patch('os.path.isfile')
    @patch(MODULE_PATH + 'InputArgument.is_valid_extension')
    def test_is_valid_argument_has_spaces(self, mock_is_valid_extension,
                                           mock_isfile, mock_file_has_no_spaces):

        """ File name has a space character in it's name """

        path_input = 'spaces in file name.txt'

        mock_isfile.return_value = True
        mock_is_valid_extension.return_value = True
        mock_file_has_no_spaces.return_value = False

        with self.assertRaises(ValueError) as context:
            self.input_argument.is_valid_argument(path_input)

        actual = str(context.exception)
        expected = 'spaces in file name.txt has spaces in file name'

        self.assertEqual(actual, expected)
        mock_isfile.assert_called_once_with(path_input)
        mock_is_valid_extension.assert_called_once_with(path_input)
        mock_file_has_no_spaces.assert_called_once_with(path_input)
