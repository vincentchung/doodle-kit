import broadlink
import sys

def SwitchOn(d):
    d.set_power(True)

def SwitchOff(d):
    d.set_power(False)

def main():
    if len(sys.argv) < 2: # 1
        print "Usage:", sys.argv[0], "\n"
        print "   on: turn on\n"
        print "   off: turn off\n"
        sys.exit(1)       # 2

    c = sys.argv[1]
    devices = broadlink.discover(timeout=15)
    devices[0].auth()

    if(c=='on'):
        print "turning on..."
        SwitchOn(devices[0])
    else:
        print "turning off..."
        SwitchOff(devices[0])

#main function
if __name__ == "__main__":
    main()
