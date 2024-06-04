#!/usr/bin/env python3
"""
    Script Documentation
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
        Method Documentation
    """
    return [collection for collection in mongo_collection.find(
        {"topics": topic}
    )]
