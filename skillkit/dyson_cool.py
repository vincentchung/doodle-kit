import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *

dysonCoolPowerSwitch="skillkit/dysoncool/powerSwitch"
dysonCoolSpinSwitch="skillkit/dysoncool/spinSwitch"

def powerOn():
    commandConnectExecute(dysonCoolPowerSwitch)

def spinOn():
    commandConnectExecute(dysonCoolSpinSwitch)
