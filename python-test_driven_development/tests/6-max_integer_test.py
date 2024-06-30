#!/usr/bin/python3

"""
6-max_integer_test.py
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_M_I(unittest.TestCase):
    """
    unittests for the function def max_integer(list=[]):
    """

    def test_ordered_list(self):
        """
        Test ordered list integers
        """
        ordered_list = [10, 20, 30, 40]
        self.assertEqual(max_integer(ordered_list), 40)

    def test_unordered_list(self):
        """
        Test an unordered list.
        """
        unordered_list = [1, 20, 4, 3]
        self.assertEqual(max_integer(unordered_list), 20)

    def test_empty_list(self):
        """
        Test empty list.
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """
        Test a list with a single element.
        """
        one_element = [10]
        self.assertEqual(max_integer(one_element), 10)

    def test_floats(self):
        """
        Test float list.
        """
        floats = [1.01, 2.54, 3.25, 4.05]
        self.assertEqual(max_integer(floats), 4.05)

    def test_negative(self):
        """
        Test float list.
        """
        negative = [-3, -10, -2, -25]
        self.assertEqual(max_integer(negative), -2)

    def test_ints_and_floats(self):
        """
        Test ints and floats.
        """
        ints_and_floats = [1, 2.05, 3, 4.78, 5]
        self.assertEqual(max_integer(ints_and_floats), 5)
    
    def test_max_at_begginning(self):
        """
        Test a list with a beginning max value.
        """
        max_at_beginning = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_string(self):
        """
        Test a string.
        """
        string = "abcde"
        self.assertEqual(max_integer(string), 'e')

    def test_list_of_strings(self):
        """
        Test list of strings.
        """
        strings = ["a", "b", "c", "d", "e"]
        self.assertEqual(max_integer(strings), "e")

    def test_empty_string(self):
        """
        Test an empty string.
        """
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
