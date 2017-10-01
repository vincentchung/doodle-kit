#import wemo_switch
import json
import sys,imp
import importlib
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
    #print skill


    if skill.find('/') > -1:
	       module,fun=skill.rsplit('/')
    else:
	       module = skill
	       fun = 'default'

    if fun == '': fun='default'
    objmodule = importlib.import_module('skillkit.'+module)
    out = getattr(objmodule, fun)()

    return out
