# -*- coding: utf-8 -*-
"""
    It runs tests
"""


import re
import unittest
import odd_word


class TestOddWord(unittest.TestCase):
    '''
        It runs tests
    '''

    def test_odd_word1(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        number = '4'
        result = odd_word.odd_word(number)
        self.assertTrue(result, re.match('[a-z]{4}', result))

    def test_odd_word2(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        number = '7'
        result = odd_word.odd_word(number)
        self.assertTrue(result, re.match('[a-z]{7}', result))

    def test_odd_word3(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        number = '1'
        result = odd_word.odd_word(number)
        self.assertTrue(result, re.match('[a-z]{1}', result))

    def test_odd_word4(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        number = '3'
        result = odd_word.odd_word(number)
        self.assertTrue(result, re.match('[a-z]{1}', result))


if __name__ == '__main__':
    unittest.main()
