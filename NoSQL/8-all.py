#!/usr/bin/env python3
"""
    Script Documentation
"""
import pymongo


def list_all(collection):
    """
        Method Documentation
    """
    if not collection:
        return []
    return list(collection.find())
