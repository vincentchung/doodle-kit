import broadlink
import sys

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
        devices[0].set_power(True)
    else:
        print "turning off..."
        devices[0].set_power(False)
#main function
if __name__ == "__main__":
    main()
