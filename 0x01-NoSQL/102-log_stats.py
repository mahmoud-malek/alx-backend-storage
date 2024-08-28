#!/usr/bin/env python3

""" a Python function that provides some stats
 about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # print num of logs
    print(collection.count(), "logs")

    # print methods
    print("Methods:")
    print(f"	method GET: {collection.count_documents({'method': 'GET'})}")
    print(f"	method POST: {collection.count_documents({'method': 'POST'})}")
    print(f"	method PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"	method PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(
        f"	method DELETE: {collection.count_documents({'method': 'DELETE'})}")
    print(
        f"{collection.count_documents({'$and': [{'method' : 'GET'},{'path': '/status'}]})} status check"
    )

    # print top 10 IPs
    print("IPs:")
    ips = collection.aggregate([{
        "$group": {
            "_id": "$ip",
            "count": {
                "$sum": 1
            }
        }
    }, {
        "$sort": {
            "count": -1
        }
    }, {
        "$limit": 10
    }])

    for ip in ips:
        print(f"	{ip.get('_id')}: {ip.get('count')}")
