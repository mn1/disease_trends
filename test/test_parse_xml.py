#!/usr/bin/python3

from parse_xml import parse_xml, parse_xml_string
import unittest

import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

data_files_dir = THIS_DIR + '/data'

class TestStringMethods(unittest.TestCase):

    def test_xml_parse_ok(self):
        
        count = parse_xml(data_files_dir + '/' + 'test.xml')
        self.assertEqual(count, "37901")

        count = parse_xml(data_files_dir + '/' + 'test_2011.xml')
        self.assertEqual(count, "176207")

        count = parse_xml(data_files_dir + '/' + 'test_2012.xml')
        self.assertEqual(count, "188997")
        
        count = parse_xml(data_files_dir + '/' + 'test_2013.xml')
        self.assertEqual(count, "196630")
        
        count = parse_xml(data_files_dir + '/' + 'test_2014.xml')
        self.assertEqual(count, "210073")
        
        count = parse_xml(data_files_dir + '/' + 'test_2015.xml')
        self.assertEqual(count, "217904")

    def test_xml_parse_from_string_ok(self):
        
        with open(data_files_dir + '/' + 'test_2011.xml') as f:
            xml_as_string = f.read()
        
        count = parse_xml_string(xml_as_string)
        self.assertEqual(count, "176207")

        with open(data_files_dir + '/' + 'test_2012.xml') as f:
            xml_as_string = f.read()
        
        count = parse_xml_string(xml_as_string)
        self.assertEqual(count, "188997")

        with open(data_files_dir + '/' + 'test_2013.xml') as f:
            xml_as_string = f.read()
        
        count = parse_xml_string(xml_as_string)
        self.assertEqual(count, "196630")

if __name__ == '__main__':
    unittest.main()