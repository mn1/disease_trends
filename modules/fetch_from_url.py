#!/usr/bin/python3

import requests as req

from construct_urls import build_esearch_url
from parse_xml      import parse_xml_string

def fetch_term_count_for_year_range(term, from_year, to_year):
    
    term_count_by_year = {}
    
    for year in range(from_year, to_year + 1):
        
        count = fetch_term_count_for_year(term, year)
        term_count_by_year[year] = count
    
    return term_count_by_year

def fetch_term_count_for_year(term, year):
    
    url = build_esearch_url(
        term = term,
        year = year
    )
    response = req.get(url)
    count_text = parse_xml_string(response.text)
    count = int(count_text)
    return count

