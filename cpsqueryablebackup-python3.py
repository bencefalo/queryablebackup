#!/usr/bin/env python3
# Ben Cefalo
# From One Atlas Cluster to another Atlas Cluster
# MongoDB 2020


import pymongo
from pymongo import MongoClient
uriSource = "mongodb+srv://username:password@SourceCluster.mongodb.net/test?retryWrites=true&w=majority"
source = pymongo.MongoClient(uriSource)
uriDest = "mongodb+srv://username:password@DestinationCluster.mongodb.net/test?retryWrites=true&w=majority"
destination = pymongo.MongoClient(uriDest)

db = source.locations
db2 = destination.locations
zips = db.zips
zips2 = db2.zips


def restore():

    start = "Finding Missing Data"
    print (start)

    query = {'state':'CO'}

    try:
        cursor = zips.find(query)

    except Exception as e:
        result = "Unexpected error:", type(e), e
        print (result)
        

    for doc in cursor:
        zips2.insert_one(doc)


if __name__ == '__main__':
    restore()
