import broadlink
import sys

def learningMode(d):
#irdata="&p7776m"
#devices[0].send_data(irdata)
#f = open('workfile', 'wb')

    while 1:
        d.enter_learning()
        filename=raw_input("enter the key name:")
        print "pressing the remote controller"
        f = open(filename, 'wb')
        irdata= None
        while(None==irdata):
            if(d.check_data()==irdata):
                irdata=None
            else:
                irdata=d.check_data()

        if(None!=irdata):
            print type(irdata)
            print len(irdata)
            print (irdata)
            f.write(irdata)
            for i in range(0, len(irdata), +1):
                print irdata[i]
            f.close()
        #devices[0].send_data(irdata)
#        d2 = bytearray(irdata)
#        print len(d2)
#        print d2[0]

def commandMode(d):
    while True:
        cmd=raw_input("enter command:")
        r = open(cmd, 'rb')
        read_data = r.read()
        d.send_data(read_data)
        r.close()


def main():
    if len(sys.argv) < 2: # 1
        print "Usage:", sys.argv[0], "\n"
        print "   l: learning mode\n"
        print "   c: command mode\n"
        sys.exit(1)       # 2

    c = sys.argv[1]
    devices = broadlink.discover(timeout=15)
    devices[0].auth()

    print devices[0].check_temperature()

    if(c=='l'):
        print "learning mode..."
        learningMode(devices[0])
    else:
        print "command mode..."
        commandMode(devices[0])

#main function
if __name__ == "__main__":
    main()
