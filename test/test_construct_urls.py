#!/usr/bin/python3

import unittest
import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

import validators

from construct_urls import build_esearch_url, build_esearch_url_year_range

class TestUrlMethods(unittest.TestCase):

    def url_ok(self, url):
        passes = validators.url(url)
        if (not passes):
            self.fail("The following url failed validation: " + url)
        return

    def test_build_esearch_url_year_range(self):
        
        urls = build_esearch_url_year_range(
            term      = "cancer",
            from_year = 2010,
            to_year   = 2015
        )
        for url in urls:
            self.url_ok(url)

    def test_build_esearch_url(self):
        
        url = build_esearch_url(
            term = "cancer",
            year = 2010,
        )
        self.url_ok(url)

if __name__ == '__main__':
    unittest.main()
