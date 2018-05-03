#!/usr/bin/python3

import _thread
from webserver import *
from broadcastService import *

def web_service():
  print("web_service")
  start_web_service()

def broadcast_service():
  print("broadcast_service")
  start_broadcast_service()

try:
   _thread.start_new_thread( broadcast_service, () )
   _thread.start_new_thread( web_service, () )
except:
   print ("Error: create thread fail")

while 1:
   pass
