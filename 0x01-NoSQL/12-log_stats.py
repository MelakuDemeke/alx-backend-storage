#!/usr/bin/env python3

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.0:27017')
    nginx_logs_collection = client.logs.nginx

    total_logs_count = nginx_logs_collection.count_documents({})
    print(f'{total_logs_count} logs')

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in http_methods:
        method_count = nginx_logs_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')
    
    status_check_count = nginx_logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check_count} status check')


