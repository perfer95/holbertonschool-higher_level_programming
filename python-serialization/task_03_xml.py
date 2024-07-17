#!/usr/bin/python3
"""
3. Serializing and Deserializing with XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serialize the dictionary into XML and save it """
    root = ET.Element('data')
    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Read the XML data from that file, and return a deserialized
    Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
