# CRUD
# create read update deleteimport requests
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.pchome
coll = db.products
#name contain ASUS
#data = coll.find({"name" : {"$regex" : ".*asus.*", "$options" : "i"}})   #條件直接用大括號   

#comparison operator 比較符號
#price > 3000
name_condition = {"name" : {"$regex" : ".*asus.*", "$options" : "i"}}
price_condition = {"price" : {"$gt" : 10000}}
#data = coll.find({"price" : {"$gt" : 3000}})


#and operator example
data = coll.find({"$and" : [name_condition, price_condition]})
# for d in data:
#     print(d["name"], d["price"])

# coll.update_one({"name" : "ASUS 華碩 ROG Strix XG32VC 32型 170Hz曲面電競螢幕"}, {"$set" : {"price" : 8000}}, upsert=True)


# coll.update_one({"name" : "Allen"}, {"$set" : {"name" : "Allen"}}, upsert=True)

coll.delete_one({"name" : "Allen"})



# insert if not exsit = upsert