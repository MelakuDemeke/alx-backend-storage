#!/usr/bin/env python3
'''
This script connects to a MongoDB database, queries an nginx logs collection,
and prints various statistics.
'''
from pymongo import MongoClient

def log_stats(nginx_logs_coll, option=None):
    '''
    This function prints statistics related to nginx logs.

    Args:
    nginx_logs_coll (pymongo.collection.Collection): The MongoDB collection
                    containing nginx logs.
    option (str, optional): An HTTP method to filter logs by. If provided,
                    statistics for that method will be printed.

    Returns:
    None
    '''
    items = {}
    if option:
        value = nginx_logs_coll.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return items

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total_logs_count = nginx_logs_coll.count_documents(items)
    print(f"{total_logs_count} logs")
    print("Methods:")
    for method in http_methods:
        log_stats(nginx_logs_coll, method)
        status_check = nginx_logs_coll.count_documents({"path": "/status"})
        print(f"{status_check} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs_coll = client.logs.nginx
    log_stats(nginx_logs_coll)
    