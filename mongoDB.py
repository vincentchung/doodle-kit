#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient


def adddata(s):
  conn = MongoClient('127.0.0.1', 27017)
  db = conn.doodleIoT
  my_set = db.sensordata
  my_set.insert(s)
#my_set.insert({"name":"zhangsan","age":18})
#users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]
#my_set.insert(users)

#for i in my_set.find():
#    print(i)

#for i in my_set.find({"name":"zhangsan"}):
#    print(i)
#print(my_set.find_one({"name":"zhangsan"}))

  conn.close()
