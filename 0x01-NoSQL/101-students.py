#!/usr/bin/env python3

""" a Python function that returns
 all students sorted by average score:
 """

import pymongo


def top_students(mongo_collection):
    """ a function to get top students
    sorted by their avg score """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {
                        "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
