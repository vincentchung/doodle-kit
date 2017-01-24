import sys
from ouimeaux.environment import Environment

switch_cmd=''

def on_switch(switch):
     global switch_cmd
     print('********  Switch found:'+ switch.name+ ', Current state : '+str(switch.get_state()))
     if(switch_cmd=='on'):
         print "turning on..."
         switch.on()
     else:
         print "turning off..."
         switch.off()

def on_motion(motion):
    print "Motion found!", motion.name


def main():
    global switch_cmd
    if len(sys.argv) < 2: # 1
        print "Usage:", sys.argv[0], "\n"
        print "   on: turn on\n"
        print "   off: turn off\n"
        sys.exit(1)       # 2

    switch_cmd=sys.argv[1]

    if(switch_cmd=='on'):
        print "turning on..."
    else:
        print "turning off..."

    env = Environment(on_switch, on_motion)
    env.start()
    env.discover(seconds=3)

#main function
if __name__ == "__main__":
    main()
