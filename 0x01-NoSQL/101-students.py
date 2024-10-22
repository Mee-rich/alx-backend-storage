#!/usr/bin/env python3
"""Top students
"""
def top_students(mongo_collection):
    """Prints all students in a collection sorted buy average score
    """
    students = mongo_collection.aggregate(
            [
                {
                    '$project':{
                        'name': 1,
                        'averageScore': {
                            '$avg': '$topics.score'
                        },
                        'topics': 1,
                    },
                },
                {
                    '$sort': {'averageScore': -1},
                },
            ]
    )
    return list(students)

