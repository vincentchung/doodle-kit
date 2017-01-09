import argparse
import imutils
import cv2
import thread
import time
#adding spport wemo
import subprocess

#declair global valuable
cap = cv2.VideoCapture(0) #openCV camera device
mCapturing = "n"
#l: learning... init the virtual button
#s: starting to monitor the button event
mCommand="l"

vb_image=list()
vb_area=list()
#min area
MINI_AREA=2000
#limist area size w*h
LIMIT_AREA_SIZE=200*200


def DBread():
    # Reading data back
    data=''
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

class eventMap( object ):
    def _jsonSupport( *args ):
        def default( self, xObject ):
            return { 'VB_id': xObject.VB_id(), 'skillkit_id': xObject.skillkit_id() }

        def objectHook( obj ):
            return skillkit( obj[ 'name' ],obj[ 'skilltype' ],obj[ 'press' ],obj[ 'release' ] )
        json.JSONEncoder.default = default
        json._default_decoder = json.JSONDecoder( object_hook = objectHook )

    _jsonSupport()


    def __init__( self, VB_id ,skillkit_id):
        self._VB_id = VB_id
        self._skillkit_id = skillkit_id

    def VB_id( self ):
        return self._VB_id
    def skillkit_id( self ):
        return self._skillkit_id

    def __repr__( self ):
        return '<skillkit(name=%s)>' % self._name

class skillkit( object ):

    def _jsonSupport( *args ):
        def default( self, xObject ):
            return { 'name': xObject.name(), 'skilltype': xObject.skilltype(),'press': xObject.press(),'release': xObject.release() }

        def objectHook( obj ):
            return skillkit( obj[ 'name' ],obj[ 'skilltype' ],obj[ 'press' ],obj[ 'release' ] )
        json.JSONEncoder.default = default
        json._default_decoder = json.JSONDecoder( object_hook = objectHook )

    _jsonSupport()

    def __init__( self, name ):
        self._name = name

    def __init__( self, name ,skilltype,press,release):
        self._name = name
        self._skilltype = skilltype
        self._press = press
        self._release = release

    def name( self ):
        return self._name
    def skilltype( self ):
        return self._skilltype
    def press( self ):
        return self._press
    def release( self ):
        return self._release

    def __repr__( self ):
        return '<skillkit(name=%s)>' % self._name

def DBupdate(obj):
    # Reading data back
    with open('data.json', 'w') as f:
        json.dump(obj, f)

def wemo_switch(b):
	if(b==0):
		cmd='wemo switch "WeMo Switch" off'
	else:
		cmd='wemo switch "WeMo Switch" on'

	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
	    print line,
	retval = p.wait()

def event_map(button_id):


def camera_scaning():
	ret, frame = cap.read()
	index=0
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	for area in vb_area:
		(x, y, w, h) = area
		cropped = gray[y:y+h,x:x+w].copy()

		#s="compare_"+repr(index)+".jpg"
		#print s + "\n"
		#cv2.imwrite( s,cropped)

		gray2 = cv2.cvtColor(vb_image[index], cv2.COLOR_BGR2GRAY)
		gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

		res = cv2.absdiff(cropped, gray2)
		thresh = cv2.threshold(res, 25, 255, cv2.THRESH_BINARY)[1]
		thresh = cv2.dilate(thresh, None, iterations=2)
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]
		c = 0
		for c in cnts:
			if(cv2.contourArea(c)>1000):
				if(index==0):
					wemo_switch(0)
				else:
					wemo_switch(1)
				print "touch!!!: " +repr(index)+":"+ repr(cv2.contourArea(c)) + "\n"

		index+=1
		#print repr area
		#print "\n"

#function for capturing image from camera
def camera_detect_vb():
	global mCapturing
	# Capture frame-by-frame
	ret, frame = cap.read()
	# Our operations on the frame come here

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,100,200)
	blurred = cv2.GaussianBlur(edges, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

	# find contours in the thresholded image and initialize the
	# shape detector
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	#sd = ShapeDetector()
	c = 0
	index=0
	#print cnts
	# loop over the contours
	for c in cnts:

		if cv2.contourArea(c) < MINI_AREA: continue
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)

		#if mCapturing == "d":
		#	print cv2.contourArea(c)
		#	shape = sd.detect_aera(c)
		#else:
		#	shape = sd.detect(c)

		if M["m00"] > 0:
			cX = int((M["m10"] / M["m00"]))
			cY = int((M["m01"] / M["m00"]))
			#c = c.astype("float")
			#c *= ratio
			c = c.astype("int")
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)
			(x, y, w, h) = cv2.boundingRect(approx)

			#area is too big
			if( w*h > LIMIT_AREA_SIZE ): continue
			#crop image!!!!
			cropped = frame[y:y+h,x:x+w].copy()
			s="cropped_"+repr(index)+".jpg"

			print s +":"+repr(cv2.contourArea(c)) + "\n"
			cv2.imwrite( s,cropped)
			vb_image.append(cropped)
			vb_area.append((x, y, w, h))
			#cv2.rectangle(frame,(x,y),(x+w,y+h), (0, 255, 0), 2)
			print "found area:"+repr(index)+" x:"+repr(x)+" y:"+repr(y)+" w:"+repr(w)+" h:"+repr(h)+"\n"
			index+=1
			#if len(approx) == 3:
			#	shape = "triangle"
			#elif len(approx) == 4:
			#	shape = "rectangle"
			#else:
			#	shape = "circle"

			#cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
			#txt=repr(index)+":"+repr(cv2.contourArea(c))
			#cv2.putText(frame, txt, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
			#	0.5, (255, 255, 255), 2)

		# show the output image
	index=0
	if mCapturing == "c":
		for area in vb_area:
			(x, y, w, h) = area
			cv2.rectangle(frame,(x,y),(x+w,y+h), (0, 255, 0), 2)
			cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
			txt=repr(index)+":"+repr(cv2.contourArea(c))
			cv2.putText(frame, txt, (x, x), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (255, 255, 255), 2)
			index+=1

		ts = time.time()
		str="leanring_vb_"+repr(ts)+".jpg"
		cv2.imwrite( str,frame)
		mCapturing="n"

	if mCapturing == "d":
		mCapturing="n"

def camera_gesture_thread( threadName, delay):
	global mCommand
	print "start camera thread!!"

	while True:
		if mCommand == "l":
			camera_detect_vb()
			mCommand= "s"
		elif mCommand == "s":
			camera_scaning()
			time.sleep(.5)


#main function
if __name__ == "__main__":
	print "starting..."
    eventobjs=list()
    #skillobjs=DBread()
    skillobjs=DBread()
    #myObject = skillkit( 'test1','cmd','pressing','releasing')
    #myObject2 = skillkit( 'test2','cmd','pressing','releasing')
    skillobjs.append(myObject)
    skillobjs.append(myObject2)
    #DBupdate(skillobjs)

    #init event mapping table
    eventobj1 = eventMap( 0,0)
    eventobj2 = eventMap( 1,1)
    eventobjs.append(eventobj1)
    eventobjs.append(eventobj2)

	mCapturing="c"
	try:
		thread.start_new_thread( camera_gesture_thread, ("Thread-1", 2, ) )
	except:
		print "Error: unable to start thread"


	while True:
		mCapturing = raw_input("press 'c' to capture picture")
		time.sleep(.1)

		#doing nothing here
