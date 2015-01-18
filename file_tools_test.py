import file_tools
import unittest


class FileToolsTests(unittest.TestCase):

    def test_get_version_part_should_return_the_first_part_correctly(self):
        part = file_tools.get_version_part("7.2.3.4", 0)
        self.assertEqual(part, 7)

    def test_get_version_part_should_return_the_second_part_correctly(self):
        part = file_tools.get_version_part("7.2.3.4", 1)
        self.assertEqual(part, 2)

    def test_get_version_part_should_return_the_third_part_correctly(self):
        part = file_tools.get_version_part("7.2.3.4", 2)
        self.assertEqual(part, 3)

    def test_get_version_part_should_return_the_fourth_part_correctly(self):
        part = file_tools.get_version_part("7.2.3.4", 3)
        self.assertEqual(part, 4)

    def test_get_version_part_should_return_None_for_index_less_than_zero(self):
        part = file_tools.get_version_part("7.2.3.4", -1)
        self.assertEqual(part, None)

    def test_get_version_part_should_return_None_for_index_greater_than_index(self):
        part = file_tools.get_version_part("7.2.3.4", 4)
        self.assertEqual(part, None)