import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *

heranACPowerSwitchON="skillkit/AC_Heran/AC_power_on"
heranACPowerSwitchOFF="skillkit/AC_Heran/AC_power_off"
heranACFan="skillkit/AC_Heran/AC_fan_change"
heranACTP="skillkit/AC_Heran/AC_temperture_"
heranACSleepMode="skillkit/AC_Heran/AC_feature_sleep"

fanLevel = 1
temperature = 25
powerButton = 0

def powerOn():
  if(powerButton==0):
    powerButton=1
    commandConnectExecute(heranACPowerSwitchON)
  else:
    powerButton=0
    commandConnectExecute(heranACPowerSwitchOFF)


def temperatureInc():
    temperature+=1
    str=heranACTP+str(temperature)
    commandConnectExecute(str)

def temperatureDec():
    temperature-=1
    str=heranACTP+str(temperature)
    commandConnectExecute(str)

def fanAirInc():
    fanLevel-=1
    if(fanLevel==0):
      fanLevel=1
    str=heranACFan+str(fanLevel)
    commandConnectExecute(str)

def fanAirDec():
    fanLevel+=1
    if(fanLevel>3):
      fanLevel=3
    str=heranACFan+str(fanLevel)
    commandConnectExecute(str)

def sleepMode():
    commandConnectExecute(heranACSleepMode)

def timerAdjInc():
    commandConnectExecute(heranACTimerInc)

def timerAdjDec():
    commandConnectExecute(heranACTimerDec)
