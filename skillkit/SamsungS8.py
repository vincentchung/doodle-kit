import mongoDB
import time
import datetime

def sensorupdate(d):
    print(d)
    a=str(d).split(",")
    timestamp = time.mktime(datetime.datetime.now())
    #adding timestamp
    data={"name":a[0],"data1":a[1]}


    mongoDB.adddata({"name":a[0],"data"+str(i):a[1i]})
    return "2"

def sensorupdate1():
    print("update")
    return "1"
