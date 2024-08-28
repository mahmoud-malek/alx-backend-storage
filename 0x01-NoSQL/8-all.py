#!/usr/bin/env python3

""" list all documents in Python """

import pymongo


def list_all(mongo_collection):
    """ list all documents in Python """
    return mongo_collection.find()
