import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *

dysonCoolPowerSwitch="dysoncool/powerSwitch"
dysonCoolSpinSwitch="dysoncool/spinSwitch"

def powerOn():
    commandConnectExecute(dysonCoolPowerSwitch)

def spinOn():
    commandConnectExecute(dysonCoolSpinSwitch)
