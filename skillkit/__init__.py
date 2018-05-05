#import wemo_switch
import json
import sys,imp
import importlib
from skillkitUtil import *
from doodle_talk import *
#from skillkit import broadlinkRM
#from skillkit import broadlinkSwitch
#from skillkit.broadlinkSwitch import SwitchOn
#for mamnaging supporting IoT devices API
#using support_list to get the list of the interface of IoT device
#so far the doodle-kit is only support on and off behavior

#m = __import__ ('foo')
#func = getattr(m,'bar')
#func()
#
#
skillkit_dat='skillkit.json'

def DBread():
    # Reading data back
    data=''
    with open(skillkit_dat, 'r') as f:
        data = json.load(f)
    return data

def getSkillkitlist():
    l=DBread()
    return l

def launchSkill(skill):
    print(skill)
    if(skill==""):
      out=getSkillkitlist()
      #module,fun=skill:.rsplit('/')
    else:
      temp=skill.rsplit('/')
      module=temp[0]
      fun=temp[1]
      chk=checkSkillkik(module,fun)
      if(chk=="no"):
        return "no"
      if(chk!="local"):
        applySkillkit("10.0.1.14",module,fun,"")
        return "not local"
      if(len(temp)>2):
        objmodule = importlib.import_module('skillkit.'+module)
        out = getattr(objmodule, fun)(temp[2])
      else:
        objmodule = importlib.import_module('skillkit.'+module)
        out = getattr(objmodule, fun)()

    return out
