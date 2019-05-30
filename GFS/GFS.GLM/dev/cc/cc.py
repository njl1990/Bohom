import json
import os
import time
import sys
import cv2
import shutil
#from pymongo import MongoClient
from PIL import Image


def CatchUSBVideo(window_name,camera_idx):
	cv2.namedWindow(window_name)
	cap = cv2.VideoCapture(camera_idx)
	while cap.isOpened():
		ok, frame = cap.read() 
		cv2.imwrite('image.catch'+'.jpg',frame)
		break
	cap.release()
	cv2.destroyAllWindows()

def CreateCaptureLog():
	CatchUSBVideo('FaceRect',0)
	crtDate=time.strftime("%Y-%m-%d", time.localtime())
	crtTime=time.strftime("%H:%M", time.localtime())
	CaptureLogData={
		'path':'image.catch',
		'date':crtDate,
		'time':crtTime,
	}
	return CaptureLogData

def SaveCaptureLog(CaptureLogData,num):
	shutil.move('image.catch.jpg','./img/imge.catch-'+str(num)+'.jpg')

def CleanCatch():
	# clean catch file
	os.remove('image.catch')

## Main
def main():
	#CaptureInterval=30*3600
	CaptureInterval=5 # for test
	i=0
	while True:
		CaptureLogData = CreateCaptureLog()
		print(CaptureLogData)
		i=i+1
		SaveCaptureLog(CaptureLogData,i)
		#CleanCatch()
		#break
		time.sleep(CaptureInterval)

if __name__ == '__main__':
	main()
