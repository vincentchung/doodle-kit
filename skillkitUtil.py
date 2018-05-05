import os
import sys
import json
import shutil

file = "skillkit.json"

def loadSkillkitJson():
  with open(file, "r") as f:
    data=f.read()
    json_data = json.loads(str(data)[0:len(str(data))])
    loadSkillkitJson=json_data
    #for i in range(len(json_data)):
      #print((json_data[i]))


def checkSkillkik(name,cmd):
  with open(file, "r") as f:
    data=f.read()
    json_data = json.loads(str(data)[0:len(str(data))])
    for i in range(len(json_data)):
      if(json_data[i]["name"]==name):
        for j in range(len(json_data[i]["command"])):
          print(json_data[i]["command"][j])
          if(json_data[i]["command"][j]==cmd):
            if(json_data[i]["devices"]=="local"):
              return "yes"
            else:
              return json_data[i]["devices"]
  return "no"

if __name__ == "__main__":
   print(checkSkillkik("wemo_swith","switch_off"))
