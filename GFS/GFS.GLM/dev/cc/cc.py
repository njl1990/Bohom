#!/usr/bin/python3
import json
import os
import time
import sys
import urllib.request
import cv2
import shutil
from bson import json_util
from pymongo import MongoClient
from PIL import Image


def CatchUSBVideo(window_name,camera_idx):
	cv2.namedWindow(window_name)
	cap = cv2.VideoCapture(camera_idx)
	while cap.isOpened():
		ok, frame = cap.read()  # 读取一帧数据
		cv2.imwrite('image.catch'+'.jpg',frame) # 存储为图像
		break
		'''
		if not ok:
			break
		# 显示图像
		cv2.imshow(window_name, frame)
		c = cv2.waitKey(1)
		if c & 0xFF == ord('q'):
			break
            # 释放摄像头并销毁所有窗口
		'''
	cap.release()
	cv2.destroyAllWindows()

def CreateCaptureLog():
	CatchUSBVideo('FaceRect',1)
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
