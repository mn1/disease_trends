#!/usr/bin/python3

# ./modules/fetch_from_url.py > test.xml

import requests as req

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=diabetes+AND+2011&datetype=pdat&retmax=100000"
resp = req.get(url)
print(resp.text)
