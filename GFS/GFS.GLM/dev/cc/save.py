from pymongo import MongoClient
from cStringIO import StringIO
import bson.binary
import json
import os
import time
import sys

## Main
def main():
	mongoClient = MongoClient('192.168.3.16',27016)
	DBClient = mongoClient['glmdb']
	collection = DBClient['glmRcd']

	path = './img'
	dirs = os.listdir(path)
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
	print('save finish')
if __name__ == '__main__':
	main()