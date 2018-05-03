#discovery doodle device and sync together
# 2018/05/03 by Vincent
#.................................

import os
import sys
import json
import shutil
import http.client

devices="devices"

if not os.path.isdir(devices):
    os.mkdir(devices)


#applySkillkit("localhost","dyson_cool","spinOn","")

#conn = http.client.HTTPConnection("localhost",8080)
#conn.request("GET", "/skillkit/dyson_cool/spinOn")
#r1 = conn.getresponse()
#print(r1.status, r1.reason)

def addDeivce(d):
  temp=devices+"\\"+d
  if not os.path.isdir(temp):
      os.mkdir(temp)
  #putting skillkit in the folder

def applySkillkit(deviceIP,module,func,param):
  conn = http.client.HTTPConnection(deviceIP,8080)
  if param=="":
   conn.request("GET", "/skillkit/"+module+"/"+func)
  else:
   conn.request("GET", "/skillkit/"+module+"/"+func+"/"+param)

  r1 = conn.getresponse()
  print(r1.status, r1.reason)


applySkillkit("localhost","dyson_cool","spinOn","")
