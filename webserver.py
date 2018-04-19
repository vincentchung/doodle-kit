#!/usr/bin/env python
import web
import os
import json
import skillkit

#control interface
#list skillkit
#setup skillkit to vitrulButton
#list vitrulButton
#images//
#get original full image / scan pattern of vitrulButton
#each block image of vitrulButton

urls = (
   '/skillkit', 'ListSkillkit',
   '/vitrulButton', 'ListSkillkit',
   '/skillkit/(.*)', 'LaunchSkillkit',
   '/images/(.*)', 'images' #this is where the image folder is located....
)

skillkit_dat='skillkit.json'

def DBread():
   # Reading data back
   data=''
   with open(skillkit_dat, 'r') as f:
     data = json.load(f)

   return data

def DBupdate(obj):
   # Reading data back
   with open('data.json', 'w') as f:
     json.dump(obj, f)

app = web.application(urls, globals())
class images:
   def GET(self,name):
     ext = name.split(".")[-1] # Gather extension

     cType = {
     "png":"images/png",
     "jpg":"images/jpeg",
     "gif":"images/gif",
     "ico":"images/x-icon"   }

     if name in os.listdir('images'):  # Security
       web.header("Content-Type", cType[ext]) # Set the Header
       return open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
     else:
       raise web.notfound()

class ListSkillkit:
   def GET(self):
     output = skillkit.getSkillkitlist()
     return output

class LaunchSkillkit:
   def GET(self, user):
     #user is the * part string...
     #trigger skillkit working
     output=skillkit.launchSkill(user)

     #output=DBread()
     return output

if __name__ == "__main__":
   app.run()
