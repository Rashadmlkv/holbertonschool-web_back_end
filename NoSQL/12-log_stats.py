#!/usr/bin/env python3
"""This module contains a Python script that provides
some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    collection = client.logs.nginx

    print(f'{collection.count_documents({})} logs\nMethods:')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status} status check')
