import json
import os
import time
import sys
import cv2
import shutil
#from pymongo import MongoClient
from cStringIO import StringIO
import bson.binary
from PIL import Image


def CatchUSBVideo(window_name,camera_idx):

	#CaptureInterval=30*3600
	CaptureInterval=5 # for test

	#cv2.namedWindow(window_name)
	cap = cv2.VideoCapture(camera_idx)

	#mongoClient = MongoClient('0.0.0.0',27016)
	#DBClient = mongoClient['glmdb']
	#collection = DBClient['glmRcd']

	while cap.isOpened():

		filename = 'image.catch.jpg'
		ok, frame = cap.read() 
		cv2.imwrite(filename,frame)
		crtDate=time.strftime("%Y-%m-%d", time.localtime())
		crtTime=time.strftime("%H:%M", time.localtime())


		with open (filename,'rb') as image:
			content = StringIO(image.read())
			SaveData={
	        	'data':bson.binary.Binary(content.getvalue()),
				'date':crtDate,
				'time':crtTime,
			}
			#collection.save(SaveData)
			print('SaveData:    date = '+SaveData['date']+'  time = '+ SaveData['time'])
		os.remove('image.catch.jpg')
		time.sleep(CaptureInterval)

		break
	cap.release()
	cv2.destroyAllWindows()


## Main
def main():
	CatchUSBVideo('cc',0)

if __name__ == '__main__':
	main()
