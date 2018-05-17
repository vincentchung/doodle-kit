import sys
sys.path.insert(0, './skillkit')
import broadlink
from broadlink import *

mDevice = None

def learningMode(d):
#irdata="&p7776m"
#devices[0].send_data(irdata)
#f = open('workfile', 'wb')

    while 1:
        d.enter_learning()
        filename=input("enter the key name:")
        print("pressing the remote controller")
        f = open(filename, 'wb')
        irdata= None
        while(None==irdata):
            if(d.check_data()==irdata):
                irdata=None
            else:
                irdata=d.check_data()

        if(None!=irdata):
            print(type(irdata))
            print(len(irdata))
            print (irdata)
            f.write(irdata)
            for i in range(0, len(irdata), +1):
                print(irdata[i])
            f.close()
        #devices[0].send_data(irdata)
#        d2 = bytearray(irdata)
#        print len(d2)
#        print d2[0]

def commandMode(d):
    while True:
        cmd=input("enter command:")
        r = open(cmd, 'rb')
        read_data = r.read()
        d.send_data(read_data)
        r.close()


def commandExecute(d,cmd):
    r = open(cmd, 'rb')
    read_data = r.read()
    d.send_data(read_data)
    r.close()

def commandConnectExecute(cmd):
    connectRM()
    r = open(cmd, 'rb')
    read_data = r.read()
    mDevice[0].send_data(read_data)
    r.close()

def getTemperature():
    connectRM()
    return mDevice[0].check_temperature()

def connectRM():
    global mDevice
    if(mDevice == None):
        print("connecting..")
        mDevice = discover(timeout=15)
        mDevice[0].auth()

    #print(mDevice[0].check_temperature())
    return mDevice;


def main():
    if len(sys.argv) < 2: # 1
        print("Usage:", sys.argv[0], "\n")
        print("   l: learning mode\n")
        print ("   c: command mode\n")
        print ("   e: execute command\n")
        sys.exit(1)       # 2

    c = sys.argv[1]
    connectRM()
    print(mDevice[0].check_temperature())

    if(c=='l'):
        print("learning mode...")
        learningMode(mDevice[0])
    elif(c=='c'):
        print("command mode...")
        commandMode(mDevice[0])
    elif(c=='e'):
        print("execute command...")
        commandExecute(mDevice[0],sys.argv[2])

#main function
if __name__ == "__main__":
    main()
