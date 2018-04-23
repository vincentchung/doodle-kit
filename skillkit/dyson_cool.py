import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *

dysonCoolPowerSwitch="skillkit/dysoncool/powerSwitch"
dysonCoolSpinSwitch="skillkit/dysoncool/spinSwitch"
dysonCoolFanDec="skillkit/dysoncool/windDown"
dysonCoolFanInc="skillkit/dysoncool/windUp"
dysonCoolTimerInc="skillkit/dysoncool/timer_inc"
dysonCoolTimerDec="skillkit/dysoncool/timer_dec"

def powerOn():
    commandConnectExecute(dysonCoolPowerSwitch)

def spinOn():
    commandConnectExecute(dysonCoolSpinSwitch)

def fanAirDec():
    commandConnectExecute(dysonCoolFanDec)

def fanAirInc():
    commandConnectExecute(dysonCoolFanInc)

def timerAdjInc():
    commandConnectExecute(dysonCoolTimerInc)

def timerAdjDec():
    commandConnectExecute(dysonCoolTimerDec)
