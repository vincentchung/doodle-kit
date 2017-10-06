import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *


panTVpowerSwitch="skillkit/panTV//panTV_power"
panTVvolumeup="skillkit/panTV/panTV_volumeup"
panTVvolumedown="skillkit/panTV/panTV_volumedown"
panTVpchannelup="skillkit/panTV/panTV_channelup"
panTVpchanneldown="skillkit/panTV/panTV_channeldown"

def powerOn():
    commandConnectExecute(panTVpowerOn)

def volumeUp():
    commandConnectExecute(panTVvolumeup)

def volumeDown():
    commandConnectExecute(panTVvolumedown)

def channelUp():
    commandConnectExecute(panTVpchannelup)

def channelDown():
    commandConnectExecute(panTVpchanneldown)
