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
	index = 0 

	while cap.isOpened():

		filename = './img/image_'+str(index)+'.jpg'
		infofilename='./img/info_'+str(index)+'.json'
		ok, frame = cap.read() 
		cv2.imwrite(filename,frame)
		crtDate=time.strftime("%Y-%m-%d", time.localtime())
		crtTime=time.strftime("%H:%M", time.localtime())

		fw = open(infofilename,'w')

		with open (filename,'rb') as image:
			content = StringIO(image.read())
			SaveData={
				'filename':filename,
				#'data':bson.binary.Binary(content.getvalue()),
				'date':crtDate,
				'time':crtTime,
			}
			fw.write(str(SaveData))
			#collection.save(SaveData)
			print('save file : '+filename + '\n' + infofilename)
		fw.close
		#os.remove('image.catch.jpg')
		index = index  + 1
		time.sleep(CaptureInterval)

		if index ==2:
			break
	cap.release()
	cv2.destroyAllWindows()


## Main
def main():
	CatchUSBVideo('cc',0)

if __name__ == '__main__':
	main()
