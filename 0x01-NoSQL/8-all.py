#!/usr/bin/env python3
""" A function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    :param mongo_collection: pymongo collection object
    :return: List of documents or an empty  list if no documents are found
    """
    documents = mongo_collection.find()

    return [document for document in documents]
