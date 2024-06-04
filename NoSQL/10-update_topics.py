#!/usr/bin/env python3
"""
    Script Documentation
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
        Method Documentation
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
