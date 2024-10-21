#!/usr/bin/env python3
"""
9. Insert a document in Python
"""
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new documnet in a collection based on kwargs

        mongo_collection: pymongo collection object
        **kwargs: other arguments
    
        return: The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return  result.inserted_id
