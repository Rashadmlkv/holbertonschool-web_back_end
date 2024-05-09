#!/usr/bin/env python3
"""Task 12"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client['logs']
    collection = db['nginx']
    num_logs = collection.count_documents({})
    print(f'{num_logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        num = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {num}')
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status} status check')
    client.close()
