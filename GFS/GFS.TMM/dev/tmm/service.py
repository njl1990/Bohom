
from bson import json_util
from bson.objectid import ObjectId
from oee.common import DateStr
from pymongo import MongoClient


class Servcie:
#Load Method 
	
	db_host = '0.0.0.0'
	db_port = 27017
	db_name = 'tmmdb'
	
	
	def LoadTmData(MachineID,Type):
	
	

		TodaySTR=DateStr.getTodayStr()
		Filter ={
			"Date":TodaySTR,
			} 


		mongoClient = MongoClient(DB.db_host,DB.db_port)
		DBClient = mongoClient[DB.db_name]
		collection = DBClient['tmmRcd']
		## load from db
		result=collection.find_all(Filter)
		MachineList=[]
		for item in result:
			MachineList.append(item)
		return MachineList
