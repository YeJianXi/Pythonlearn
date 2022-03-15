#!/usr/bin/python3
 
import pymongo

#!/usr/bin/python3
 
import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]

# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
# dblist = myclient.list_database_names()
# # dblist = myclient.database_names() 
# if "runoobdb" in dblist:
#   print("数据库已存在！")


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
 
mycol = mydb["sites"]