#!/usr/bin/env python3
# Ben Cefalo
# MongoDB August 2019


import pymongo
from pymongo import MongoClient
sourceUri = "mongodb://localhost:27017"
source = pymongo.MongoClient(sourceUri)
destinationUri = "mongodb+srv://<userName>:<passWord>@<mongodb_instance>/test?retryWrites=true&w=majority"
destination = pymongo.MongoClient(destinationUri)

db = source.locations
db2 = destination.locations
zips = db.zips
zips2 = db2.zips


def restore():

    start = "Finding Missing Data" 
    print (start)

    query = {'state': 'VT'}

    try:
        cursor = zips.find(query)

    except Exception as e:
        result = "Unexpected error:", type(e), e 
        print (result)

    for doc in cursor:
        zips2.insert_one(doc)


if __name__ == '__main__':
    restore()
