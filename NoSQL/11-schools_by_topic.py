#!/usr/bin/env python3
"""Task 11"""


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic"""
    return list(mongo_collection.find({ "topics": topic}))
