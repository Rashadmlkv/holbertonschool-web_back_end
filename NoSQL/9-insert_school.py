#!/usr/bin/env python3
"""Task 9"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    new = mongo_collection.insert(kwargs)
    return new
