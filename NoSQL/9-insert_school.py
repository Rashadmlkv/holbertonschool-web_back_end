#!/usr/bin/env python3
"""
    Script Documentation
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        Method Documentation
    """
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
