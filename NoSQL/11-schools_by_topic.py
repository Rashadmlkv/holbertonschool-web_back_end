#!/usr/bin/env python3
"""This module contains a Python function that returns
the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}})
