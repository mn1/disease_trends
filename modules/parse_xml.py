#!/usr/bin/python3

import xml.etree.ElementTree

def parse_xml(file_name):
    
    e = xml.etree.ElementTree.parse(file_name).getroot()
    
    expected_root_element = "eSearchResult"
    
    if (e.tag != expected_root_element):
        raise Exception("XML parse error: root element is not %s" % (expected_root_element));
    
    count_field_name = "Count"
    
    count_element = e.find(count_field_name)
    
    if (count_element is None):
        raise Exception("XML parse error: Could not find field with count: %s" % (count_field_name));
    return count_element.text

