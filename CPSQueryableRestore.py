#!/usr/bin/env python
# Benjamin Cefalo
# From One Atlas Cluster to another Atlas Cluster
# Copyright MongoDB April 2020


import pymongo
from pymongo import MongoClient
uriSource = "mongodb+srv://DBuser:pass@source.mongodb.net/test?retryWrites=true&w=majority"
source = pymongo.MongoClient(uriSource)
uriDest = "mongodb+srv://DBuser:pass@dest-cluster.mongodb.net/test?retryWrites=true&w=majority"
destination = pymongo.MongoClient(uriDest)

db = source.dbName
db2 = destination.dbName
zips = db.collectionName
zips2 = db2.collectionName


def restore():

    print "Finding Missing Data"

    query = {QUERY}

    try:
        cursor = dbSource.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        dbDestination.insert(doc)


if __name__ == '__main__':
    restore()
