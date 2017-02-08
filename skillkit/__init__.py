import wemo_switch
import json
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
    out=''
    if(skill=='wemo_switch.off'):
        out=wemo_switch.switch_off()
    elif(skill=='wemo_switch.on'):
        out=wemo_switch.switch_on()

    return out
