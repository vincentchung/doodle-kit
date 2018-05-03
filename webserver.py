#!/usr/bin/env python
import web
import os
import json
import skillkit
#from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

#control interface
#list skillkit
#setup skillkit to vitrulButton
#list vitrulButton
#images//
#get original full image / scan pattern of vitrulButton
#each block image of vitrulButton

#key needs to be 16 bytes
web_key='kkkkkkkkkkkkkkkk'

urls = (
   '/skillkit', 'ListSkillkit',
   '/vitrulButton', 'ListSkillkit',
   '/skillkit/(.*)', 'LaunchSkillkit',
   '/images/(.*)', 'images' #this is where the image folder is located....
)

skillkit_dat='skillkit.json'

def getwebKey():
    return web_key

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

class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

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

def start_web_service():
   app.run()

if __name__ == "__main__":
   start_service()
