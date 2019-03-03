#!/usr/bin/python3

import unittest
import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

from fetch_from_url \
    import \
        fetch_term_count_for_year, \
        fetch_term_count_for_year_range

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class TestFetchMethods(unittest.TestCase):

    def test_fetch_term_count_for_year(self):
        
        count = fetch_term_count_for_year("cancer", 2010)
        self.assertTrue(RepresentsInt(count))

    def test_fetch_term_count_for_year(self):
        
        counts = fetch_term_count_for_year_range("cancer", 2010, 2012)
        
        self.assertTrue( RepresentsInt(counts[2010]) )
        self.assertTrue( RepresentsInt(counts[2011]) )
        self.assertTrue( RepresentsInt(counts[2012]) )

if __name__ == '__main__':
    unittest.main()
