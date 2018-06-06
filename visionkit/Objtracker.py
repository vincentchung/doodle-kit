# USAGE
# python track.py --video video/iphonecase.mov

# import the necessary packages
#import numpy as np
import argparse
import time
import cv2
import datetime

#config
minarea=80
#the delay of each frame
frame_delay=0.025
#the define of "silent" time to stop recording
#the counting frame for no object moving
silentLimit=30

#global value
firstFrame = None
objcount=0
faceCurrentNum=0
faceRects=None
start_recording=0
no_tricker_counter=0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
face_cascade="haarcascade_frontalface_default.xml"
recording_fps=20.0

class FaceDetector:
	def __init__(self, faceCascadePath):
		# load the face detector
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):
		# detect faces in the image
		rects = self.faceCascade.detectMultiScale(image,
			scaleFactor = scaleFactor, minNeighbors = minNeighbors,
			minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

		# return the rectangles representing bounding
		# boxes around the faces
		return rects


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face",
	help = "path to where the face cascade resides")

ap.add_argument("-v", "--video",
	help = "path to the (optional) video file")
args = vars(ap.parse_args())

if args.get("face", False):
	face_cascade = args["face"]

fd = FaceDetector(face_cascade)

if not args.get("video", False):
	camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# check to see if we have reached the end of the
	# video
	if not grabbed:
		break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (3, 3), 0)

	if firstFrame is None:
		firstFrame = gray
		continue

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)
	(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


	largestarea=0
	x=0
	y=0
	w=0
	h=0

	area_counter=0;
	for c in cnts:
		#print(cv2.contourArea(c))
		if(cv2.contourArea(c)>minarea):
			area_counter+=1
			#print(cv2.contourArea(c))
			(x,y,w,h) = cv2.boundingRect(c)
			#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
		if(cv2.contourArea(c)>largestarea):
			(x,y,w,h) = cv2.boundingRect(c)

	if(start_recording==1):
		out.write(frame)

	#cv2.putText(frame, (str(cv2.contourArea(c))), (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
	if objcount != area_counter:
		no_tricker_counter=0
		if(start_recording==0):
			start_recording=1
			#fps = camera.get(cv2.CAP_PROP_FPS) <-return 0.0
			size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
			#print("fps:"+str(fps)+",size:"+str(size))
			#out = cv2.VideoWriter(str(int(time.time()))+'.avi',fourcc, 20.0, (640,480))
			out = cv2.VideoWriter(str(int(time.time()))+'.avi',fourcc, recording_fps, size)
			print("trigger!!:"+str(objcount))

		firstFrame=gray
		objcount=area_counter
        # find faces in the image
			#faceframe=frame[y:y + h,x:x + w]
		faceframe=gray
		#faceRects = fd.detect(faceframe, scaleFactor = 1.1, minNeighbors = 5,minSize = (30, 30))
		faceRects = fd.detect(faceframe)

		if(len(faceRects)>0):
			print("I found {} face(s)".format(len(faceRects)))
			faceCurrentNum=len(faceRects)
		else:
			faceCurrentNum=0
		# loop over the faces and draw a rectangle around each
		#for (fx, fy, w, h) in faceRects:
		#	cv2.rectangle(frame, (x+fx, y+fy), (x+fx + w, y+fy + h), (255, 0, 0), 1)
	else:
		no_tricker_counter+=1

	if(faceCurrentNum>0):
		for (fx, fy, w, h) in faceRects:
			cv2.rectangle(frame, (fx, fy), (fx + w, fy + h), (255, 0, 0), 1)


	cv2.putText(frame, ("face:"+str(faceCurrentNum)), (0, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
# show the frame and the binary image
	cv2.imshow("Tracking", frame)
#	cv2.imshow("Binary", thresh)

	time.sleep(frame_delay)

	if(no_tricker_counter>silentLimit and start_recording==1):
		start_recording=0
		out.release()
	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
