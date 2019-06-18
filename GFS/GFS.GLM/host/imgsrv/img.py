import os
import time
import sys
from pymongo import MongoClient


def download(list):
	mongoClient = MongoClient('db',27016)
	DBClient = mongoClient['glmdb']
	collection = DBClient['glmRcd']
	result=collection.find({'_id':{'$nin':list}})
	print(result)
	imgList=[]
	for item in result:
		static_path = '/home/bowen/git/Bohom/GFS/GFS.GLM/dev/clweb/dev/static/assets/images/glm/'
		imgfile = os.path.normcase(static_path+str(item['_id'])+'.jpg')
		print(imgfile)
		if not os.path.exists(imgfile):
			imgList.append(item['_id'])
			print('download to :'+ str(item['_id'])+'.jpg')
			fw = open(imgfile,'wb')
			byteCount = fw.write(item['data'])
			fw.close()
		#break
	return imgList



## Main
def main():
	list =[]
	while 1:
		print('downloading images...')
		list = download(list)
		print('add file')
		print(list)
		time.sleep(10)
		break



if __name__ == '__main__':
	main()
