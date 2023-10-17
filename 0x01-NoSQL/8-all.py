#!/usr/bin/env python3

def list_all(mongo_collection):
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []
    return documents
