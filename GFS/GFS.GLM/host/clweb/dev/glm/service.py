from bson import json_util
from bson.objectid import ObjectId
from pymongo import MongoClient
from django.conf import settings
import os


class GlmService:
#Load Method 
	def LoadDbData():
		print('service')
		imgList=[]
		'''
		mongoClient = MongoClient('db',27017)
		DBClient = mongoClient['glmdb']
		collection = DBClient['glmRcd']
		result=collection.find({})

		
		for item in result:
			imgList.append(str(item['_id'])+'.jpg')
		'''
		print(imgList)
		return imgList
		
	def remove():
		mongoClient = MongoClient('172.20.10.3',27016)
		DBClient = mongoClient['glmdb']
		collection = DBClient['glmRcd']
		collection.remove({})
		print('ok')

#GlmService.LoadDbData()
