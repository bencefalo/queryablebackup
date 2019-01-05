#!/usr/bin/env python
# Ben Cefalo
# MongoDB 2018


import pymongo
from pymongo import MongoClient
source = pymongo.MongoClient("mongodb://localhost:27017")
uri = "mongodb+srv://<USERNAME>:<PASSWORD>@<mongodb_instance>/test?retryWrites=true"
destination = pymongo.MongoClient(uri)

db = source.locations
db2 = destination.locations
zips = db.zips
zips2 = db2.zips


def restore():

    print "Finding Missing Data"

    query = {'state': 'CO'}

    try:
        cursor = zips.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        zips2.insert(doc)


if __name__ == '__main__':
    restore()
