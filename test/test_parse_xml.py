#!/usr/bin/python3

from parse_xml import parse_xml
import unittest

import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class TestStringMethods(unittest.TestCase):

    def test_xml_parse_ok(self):
        
        count = parse_xml(THIS_DIR + '/' + 'test.xml')
        self.assertEqual(count, "37901")

        count = parse_xml(THIS_DIR + '/' + 'test_2011.xml')
        self.assertEqual(count, "176207")

        count = parse_xml(THIS_DIR + '/' + 'test_2012.xml')
        self.assertEqual(count, "188997")
        
        count = parse_xml(THIS_DIR + '/' + 'test_2013.xml')
        self.assertEqual(count, "196630")
        
        count = parse_xml(THIS_DIR + '/' + 'test_2014.xml')
        self.assertEqual(count, "210073")
        
        count = parse_xml(THIS_DIR + '/' + 'test_2015.xml')
        self.assertEqual(count, "217904")

if __name__ == '__main__':
    unittest.main()