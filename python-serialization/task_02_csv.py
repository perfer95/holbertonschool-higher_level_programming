#!/usr/bin/python3
"""
2. Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_file_name):
    """
    Takes the CSV filename as its parameter and writes the JSON data to JSON
    """
    try:
        with open(csv_file_name, 'r', encoding="utf-8") as csv_file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        with open('data.json', 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        
        return True

    except FileNotFoundError:
        return False
