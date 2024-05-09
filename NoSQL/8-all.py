#!/usr/bin/env python3
"""Task 8"""
import pymongo


def list_all(mongo_collection):
    """Lists all the docs in a collection"""
    docs = mongo_collection.find()
    if docs.count() == 0:
        return []
    return docs
