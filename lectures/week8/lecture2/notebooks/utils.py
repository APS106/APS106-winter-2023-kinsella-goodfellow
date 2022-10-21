"""
utils.py
This file contains helper functions for Assignment 3.
Author: Sebastian D. Goodfellow
"""

# 3rd party imports
import json


def dict_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def load_data():
    return json.load(open('data.json'))
