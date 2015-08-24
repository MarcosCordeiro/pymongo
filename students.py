import pymongo
import sys

from pymongo import MongoClient

# Copyright 2014
# Author: JJFT

# connnecto to the db on standard port
connection = MongoClient('localhost',27017)


db = connection.school       # attach to db
collection = db.students         # specify the colllection

print db
print collection

query = {'scores.type':'homework'}

try:
    cursor = collection.find(query)
    for doc in cursor:
        scores = doc['scores']
        idd = doc['_id']
        print idd
        scoAnt = 0
        for scr in scores:
            if (scr['type'] == "homework"):
                if (scoAnt == 0): scoAnt = scr['score']
                print scr,',',scr['type'],',',scr['score']
                if (scr['score'] < scoAnt): scoAnt = scr['score']
        print scoAnt
        cond = {"$and" : [{'_id' : idd},{ 'scores.type' : "homework"}] }
        query = { '$pull': { 'scores': { "score": scoAnt } } }
        collection.update( cond,query,multi=False)
        print doc 

except:
    # print ("Error trying to read collection:" + sys.exc_info()[0])
        print ("Error trying to read collection:")