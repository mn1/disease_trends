#!/usr/bin/python3

def build_esearch_url_year_range(
        esearch_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        term             = "diabetes",
        from_year        = 2011,
        to_year          = 2015,
        retmax           = 100000
    ):
    urls = [ 
        build_esearch_url(
            esearch_base_url,
            term,
            year,
            retmax
        ) 
            for year in range(from_year, to_year + 1) 
    ]
    return urls

def build_esearch_url(
        esearch_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        term             = "diabetes",
        year             = 2011,
        retmax           = 100000
    ):
    url = "%s?db=pubmed&term=%s+AND+%s&datetype=pdat&retmax=%s" % ( esearch_base_url, term, year, retmax)
    return url
