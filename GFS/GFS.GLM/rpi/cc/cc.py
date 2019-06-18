import os
import time
import sys
import cv2
from PIL import Image


def CatchUSBVideo(window_name,camera_idx):

	#CaptureInterval=30*3600
	CaptureInterval=5 # for test

	cap = cv2.VideoCapture(camera_idx)
	index = 0 

	while cap.isOpened():
		APP_PATH='/usr/local/gfs/glm/rpi'
		filename = APP_PATH+'/data/image_'+str(index)+'.jpg'
		infofilename=APP_PATH+'/data/info_'+str(index)+'.json'
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

		if index ==5:
			break
	cap.release()
	cv2.destroyAllWindows()


## Main
def main():
	CatchUSBVideo('cc',0)

if __name__ == '__main__':
	main()
