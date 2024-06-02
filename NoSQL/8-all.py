#!/usr/bin/env python3
"""This module contains a Python function that
lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    
    return mongo_collection.find()
