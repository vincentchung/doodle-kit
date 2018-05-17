import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *

heranACPowerSwitch="skillkit/AC_Heran/AC_power_on"
heranACSpinSwitch="skillkit/AC_Heran/spinSwitch"
heranACFanDec="skillkit/AC_Heran/windDown"
heranACFanInc="skillkit/AC_Heran/windUp"
heranACTP24="skillkit/AC_Heran/AC_temperture_24"
heranACTP25="skillkit/AC_Heran/AC_temperture_25"

def powerOn():
    commandConnectExecute(heranACPowerSwitch)

def temperatureInc():
    commandConnectExecute(heranACTP24)

def temperatureDec():
    commandConnectExecute(heranACTP25)

def fanAirInc():
    commandConnectExecute(heranACFanInc)

def timerAdjInc():
    commandConnectExecute(heranACTimerInc)

def timerAdjDec():
    commandConnectExecute(heranACTimerDec)
