#!/usr/bin/env python3
'''
This script connects to a MongoDB database, queries an nginx logs collection,
and prints various statistics.
'''
from pymongo import MongoClient

if __name__ == "__main__":
    '''
    This is the main part of the script where it connects to a MongoDB database
    queries an nginx logs collection, and prints various statistics.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs_collection = client.logs.nginx

    total_logs_count = nginx_logs_collection.count_documents({})
    print(f'{total_logs_count} logs')

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('methods:')
    for method in http_methods:
        method_count = nginx_logs_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    status_check_count = nginx_logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check_count} status check')
