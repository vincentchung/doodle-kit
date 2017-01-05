import argparse
import imutils
import cv2
import thread
import time

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
				print "touch!!!: " + repr(cv2.contourArea(c)) + "\n"

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
			#crop image!!!!
			cropped = frame[y:y+h,x:x+w].copy()
			s="cropped_"+repr(index)+".jpg"
			index+=1
			print s + "\n"
			cv2.imwrite( s,cropped)
			vb_image.append(cropped)
			vb_area.append((x, y, w, h))
			cv2.rectangle(frame,(x,y),(x+w,y+h), (0, 255, 0), 2)
			#if len(approx) == 3:
			#	shape = "triangle"
			#elif len(approx) == 4:
			#	shape = "rectangle"
			#else:
			#	shape = "circle"

			#cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
			#txt=shape+":"+repr(cv2.contourArea(c))
			#cv2.putText(frame, txt, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
			#	0.5, (255, 255, 255), 2)

		# show the output image
	if mCapturing == "c":
		cv2.imwrite( "output.jpg",frame)
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


#main function
if __name__ == "__main__":
	print "starting..."
	mCapturing="n"
	try:
		thread.start_new_thread( camera_gesture_thread, ("Thread-1", 2, ) )
	except:
		print "Error: unable to start thread"


	while True:
		mCapturing = raw_input("press 'c' to capture picture")
		time.sleep(.1)

		#doing nothing here
