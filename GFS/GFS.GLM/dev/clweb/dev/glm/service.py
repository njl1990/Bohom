from bson import json_util
from bson.objectid import ObjectId
from pymongo import MongoClient
from django.conf import settings
import os


class GlmService:
#Load Method 
	def LoadDbData():
		print('service')

		mongoClient = MongoClient('172.20.10.3',27016)
		DBClient = mongoClient['glmdb']
		collection = DBClient['glmRcd']
		result=collection.find({})
		imgList=[]
		i=1
		for item in result:
			imgfile = os.path.normcase(os.path.abspath('..')+'\\static\\assets\\images\\glm\\'+str(item['_id'])+'.jpg')
			print(imgfile)
			if not os.path.exists(imgfile):
				imgList.append(str(item['_id'])+'.jpg')
				fw = open(imgfile,'wb')
				byteCount = fw.write(item['data'])
				fw.close()
				#print(item)
				i=i+1
			#break
		return imgList

	def remove():
		mongoClient = MongoClient('172.20.10.3',27016)
		DBClient = mongoClient['glmdb']
		collection = DBClient['glmRcd']
		collection.remove({})
		print('ok')

#GlmService.LoadDbData()
#GlmService.remove()