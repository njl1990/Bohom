import os
import time
import sys
import cv2
from PIL import Image


def CatchUSBVideo(window_name,camera_idx,index):

	#CaptureInterval=30*3600
	CaptureInterval=30 # for test

	cap = cv2.VideoCapture(camera_idx)
	while cap.isOpened():
		IMAGE_PATH='/images'
		INFO_PATH='/info'
		
		filename = IMAGE_PATH+'/image_'+str(index)+'.jpg'
		infofilename=INFO_PATH+'/info_'+str(index)+'.json'
		ok, frame = cap.read() 
		cv2.imwrite(filename,frame)
		crtDate=time.strftime("%Y-%m-%d", time.localtime())
		crtTime=time.strftime("%H:%M", time.localtime())
		fw = open(infofilename,'w')
		with open (filename,'rb') as image:
			SaveData={
				'filename':filename,
				'date':crtDate,
				'time':crtTime,
			}
			fw.write(str(SaveData))
			print('save file : '+filename + '\n' + infofilename)
		fw.close
		index = index  + 1
		time.sleep(CaptureInterval)
	cap.release()
	cv2.destroyAllWindows()

## Main
def main():
	index = 0 
	while 1:
		try:
			CatchUSBVideo('cc',0,index)
		except Exception as e:
			print(e)

if __name__ == '__main__':
	main()
