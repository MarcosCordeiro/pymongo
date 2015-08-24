import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost',27017)

db = connection.test

names = db.nomes

item = names.find_one()

print item['cidade']