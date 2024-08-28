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
    print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(
        f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")
    print(
        f"{collection.count_documents({'$and': [{'method' : 'GET'},{'path': '/status'}]})} status check"
    )

    # print top 10 IPs
    print("IPs:")
    top_ips = collection.aggregate([{
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

    for ip in top_ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
