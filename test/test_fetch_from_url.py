#!/usr/bin/python3

import unittest
import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

from fetch_from_url \
    import \
        fetch_term_count_for_year, \
        fetch_term_count_for_year_range

class TestFetchMethods(unittest.TestCase):

    def test_fetch_term_count_for_year(self):
        
        count = fetch_term_count_for_year("cancer", 2010)
        self.assertEqual(count, 167665)

    def test_fetch_term_count_for_year(self):
        
        counts = fetch_term_count_for_year_range("cancer", 2010, 2012)
        
        self.assertEqual(counts[2010], 167665)
        self.assertEqual(counts[2011], 176218)
        self.assertEqual(counts[2012], 189013)
        # print(counts);
        #
        # counts = {2010: 167665, 2011: 176218, 2012: 189013}

if __name__ == '__main__':
    unittest.main()
