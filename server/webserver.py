#!/usr/bin/env python
import web
import os
import xml.etree.ElementTree as ET

tree = ET.parse('user_data.xml')
root = tree.getroot()

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
	output = 'users:[';
	for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
	output += ']';
        return output

class get_user:
    def GET(self, user):
	for child in root:
		if child.attrib['id'] == user:
		    return str(child.attrib)

if __name__ == "__main__":
    app.run()
