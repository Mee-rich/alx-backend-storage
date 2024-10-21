#!/usr/bin/env python3
"""
10. Change school topics
"""
def update_topics(mongo_collection, name, topics):
    """ Changes all the topics of a school document based on the name
        mongo_colection: The pymongo collection object
        name(str): The school name to update
        topics(str): The list of topics approached in the school
    """
    db = mongo_collection
    result = db.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )
    return result
