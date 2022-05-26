# -*- coding: utf-8 -*-
"""
    It runs tests
"""


import unittest
import distinct_letters_match_count as solution


class TestSolution(unittest.TestCase):
    '''
        It runs tests
    '''

    def test_solution1(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        sequence = 'aaaabbbb'
        result = solution.distinct_letters_match_count(sequence)
        self.assertEqual(result, 1)

    def test_solution2(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        sequence = 'ccaaffddecee'
        result = solution.distinct_letters_match_count(sequence)
        self.assertEqual(result, 6)

    def test_solution3(self):
        """
            It runs the code with pre-defined value and compare result with expected result
        """
        sequence = 'eeee'
        result = solution.distinct_letters_match_count(sequence)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
