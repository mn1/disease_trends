#!/usr/bin/python3

import xml.etree.ElementTree

def parse_xml(file_name):
    
    e = xml.etree.ElementTree.parse(file_name).getroot()
    return _get_count_from_element_tree(e)

def parse_xml_string(xml_string):
    
    e = xml.etree.ElementTree.fromstring(xml_string)
    return _get_count_from_element_tree(e)
    
def _get_count_from_element_tree(e):
    expected_root_element = "eSearchResult"
    
    if (e.tag != expected_root_element):
        raise Exception("XML parse error: root element is not %s" % (expected_root_element));
    
    count_field_name = "Count"
    
    count_element = e.find(count_field_name)
    
    if (count_element is None):
        raise Exception("XML parse error: Could not find field with count: %s" % (count_field_name));
    return count_element.text
