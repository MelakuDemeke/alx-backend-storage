#!/usr/bin/env python3

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.0:27017')
    nginx_logs_collection = client.logs.nginx
