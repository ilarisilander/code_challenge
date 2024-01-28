""" Test cases for the Files module """

import unittest

from libraries.Files import TextFile
from unittest.mock import patch


class TestTextFile(unittest.TestCase):

    def setUp(self):
        self.text_file = TextFile('c:/dummy_path/dummy_file.txt')
        self.text_file.name = 'dummy_file'

    def test_count_words_in_list(self):
        test_list = ['dummy_file', '"dummy_file"', '(dummy_file)',
                     'hello', 'world', 'hello_DUMMY_FILE']

        expected = 4
        actual = self.text_file.count_words_in_list(test_list)

        self.assertEqual(expected, actual)

    @patch('builtins.open',
           new_callable=unittest.mock.mock_open,
           read_data='Hello World and everybody')
    def test_file_content_to_list(self, mock_open):
        expected = ['Hello', 'World', 'and', 'everybody']
        actual = self.text_file.file_content_to_list()

        self.assertEqual(expected, actual)

    def test_get_name_from_file_path(self):
        expected = 'dummy_file'
        actual = self.text_file.get_name_from_file_path()

        self.assertEqual(expected, actual)

    def test_set_name(self):
        expected = 'new_name'
        self.text_file.set_name('new_name')
        actual = self.text_file.name

        self.assertEqual(expected, actual)
