import mongoDB
import time
import datetime

def sensorupdate(d):
    print(d)
    a=str(d).split(",")
    timestamp = time.mktime(time.localtime())
    #adding timestamp
    data={"name":a[0],"data1":a[1]}


    mongoDB.adddata({"name":a[0],"data":a[1]})
    return "2"

def sensorupdate1():
    print("update")
    return "1"
