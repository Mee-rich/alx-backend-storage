#!/usr/bin/env python3
""" Task 11 """

def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specified topic
        
        mongo_collection: The pymongo collection object
        topic (str): The topic searched
    """
    topic_filter = {
            'topics': {
                '$elemMatch': {
                    '$eq': topic,
                    },
                },
            }
    documents = mongo_collection.find(topic_filter)
    return [doc for doc in documents]
