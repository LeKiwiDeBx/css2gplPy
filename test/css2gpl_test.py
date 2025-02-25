# test_css2gpl.py

import json
import unittest

from numpy.testing import assert_array_equal
from css2gpl import extract_comment, extract_hexa, extract_hexa_list, color_name2rgb, extract_color_named, hsl2Rgb

class TestExtractComment(unittest.TestCase):
    def setUp(self):
        with open('test/test_cases.json') as f:
            self.test_data = json.load(f)

    def test_extract_comment(self):
        for test_case in self.test_data['tests_comments']:
            input_css = test_case['input']
            expected_output = test_case['expected']
            self.assertEqual(extract_comment(input_css), expected_output)
    
    
    def test_extract_hexa(self):
        for test_case in self.test_cases:
            input_css = test_case['input']
            expected_output = test_case['expected']
            self.assertEqual(extract_hexa(input_css), expected_output)


    def test_extract_hexa(self):
        for test_case in self.test_data['tests_hexa']:
            input_css = test_case['input']
            expected_output = test_case['expected']
            self.assertEqual(extract_hexa(input_css), expected_output)

    def test_extract_hexa_list(self):
        for test_case in self.test_data['tests_hexa_list']:
            input_css = test_case['input']
            expected_output = test_case['expected']
            assert_array_equal(extract_hexa_list(input_css), expected_output)

    def test_color_name2rgb(self):
        for test_case in self.test_data['tests_color_name2rgb']:
            input_css = test_case['input']
            expected_output = test_case['expected']
            self.assertEqual(color_name2rgb(input_css), expected_output)


    def test_extract_color_named(self):
        for test_case in self.test_data['tests_extract_color_named']:
            input_css = test_case['input']
            expected_output = test_case['expected']
            assert_array_equal(extract_color_named(input_css), expected_output)

    def test_hsl2Rgb(self):
        for test_case in self.test_data['tests_hsl2Rgb']:
            input_h = test_case['h']
            input_s = test_case['s']
            input_l = test_case['l']
            expected_output = test_case['expected']
            self.assertEqual(hsl2Rgb(input_h, input_s, input_l), expected_output)

if __name__ == "__main__":
    unittest.main()
