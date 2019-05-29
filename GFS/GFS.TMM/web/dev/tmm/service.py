from bson import json_util
from bson.objectid import ObjectId
from tmm.common import DateStr
from pymongo import MongoClient


class TmmServcie:
#Load Method 
	def LoadTmData():
		print('service')
		TodaySTR=DateStr.getTodayStr()
		Filter={"date":TodaySTR} 
		mongoClient = MongoClient('0.0.0.0',27017)
		DBClient = mongoClient['tmmdb']
		collection = DBClient['tmmRcd']
		result=collection.find(Filter)
		tmmRcdList=[]

		for item in result:
		    tmmRcdList.append(item)
		return tmmRcdList
