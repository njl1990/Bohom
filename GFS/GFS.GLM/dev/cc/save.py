from pymongo import MongoClient
from cStringIO import StringIO
import bson.binary
import json
import os
import time
import sys
#from PIL import Image


def CatchUSBVideo(window_name,camera_idx):

	#CaptureInterval=30*3600
	CaptureInterval=5 # for test

	#cv2.namedWindow(window_name)
	cap = cv2.VideoCapture(camera_idx)



	while cap.isOpened():

		filename = 'image.catch.jpg'
		ok, frame = cap.read() 
		cv2.imwrite(filename,frame)
		#crtDate=time.strftime("%Y-%m-%d", time.localtime())
		#crtTime=time.strftime("%H:%M", time.localtime())
		'''
		with open (filename,'rb') as image:
			content = StringIO(image.read())
			SaveData={
				'data':bson.binary.Binary(content.getvalue()),
				'date':crtDate,
				'time':crtTime,
			}
			#collection.save(SaveData)
			print('SaveData:    date = '+SaveData['date']+'  time = '+ SaveData['time'])
		'''
		#os.remove('image.catch.jpg')
		time.sleep(CaptureInterval)

		break
	cap.release()
	cv2.destroyAllWindows()


## Main
def main():
	mongoClient = MongoClient('192.168.3.16',27016)

	DBClient = mongoClient['glmdb']
	collection = DBClient['glmRcd']

	path = './img'
	dirs = os.listdir(path)
	fwspath = './img/save.result'
	fws=open(fwspath,'w')
	for file in dirs:
		name = os.path.basename(file)
		if '.json' in name:
			fr = open(path+'/'+name,'r')
			# find the info.json
			infoJson=fr.read()
			print(infoJson)
			infoData = json.loads(infoJson.replace("'", '"'))
			filename=infoData['filename']
			crtDate=infoData['date']
			crtTime=infoData['time']

			with open (filename,'rb') as image:
				content = StringIO(image.read())
				SaveData={
					'data':bson.binary.Binary(content.getvalue()),
					'date':crtDate,
					'time':crtTime,
				}
				collection.save(SaveData)
				print('SaveData:    date = '+SaveData['date']+'  time = '+ SaveData['time'])
			fr.close()
			fws.write(filename)
			fws.write(path+'/'+name)	
	print('save finish')
	fws.close()
if __name__ == '__main__':
	main()
