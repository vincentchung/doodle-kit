import sys
sys.path.insert(0, './skillkit')
from broadlinkRM import *

def getTemp():
  print(getTemperature())
  return getTemperature()
