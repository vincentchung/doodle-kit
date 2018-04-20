import mongoDB

def sensorupdate(d):
    print(d)
    mongoDB.adddata({"name":"zhangsan","age":18})
    return "2"

def sensorupdate1():
    print("update")
    return "1"
