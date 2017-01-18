#!/usr/bin/env python
import web
import os
import  json

#control interface
#list skillkit
#setup skillkit to vitrulButton
#list vitrulButton
#images//
#get original full image / scan pattern of vitrulButton
#each block image of vitrulButton

urls = (
    '/skillkit', 'list_users',
    '/vitrulButton', 'list_users',
    '/vitrulButton/(.*)', 'get_user',
    '/images/(.*)', 'images' #this is where the image folder is located....
)


def DBread():
    # Reading data back
    data=''
    with open('data.json', 'r') as f:
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
            "ico":"images/x-icon"            }

        if name in os.listdir('images'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()

class list_users:
    def GET(self):
	output = '[{"press": "pressing", "release": "releasing", "name": "test1", "skilltype": "cmd"}, {"press": "pressing", "release": "releasing", "name": "test2", "skilltype": "cmd"}, {"press": "pressing", "release": "releasing", "name": "test1", "skilltype": "cmd"}, {"press": "pressing", "release": "releasing", "name": "test2", "skilltype": "cmd"}]'
        return output

class get_user:
    def GET(self, user):
        output=DBread()
        return output

if __name__ == "__main__":
    app.run()
