# stop docker 
#sudo docker stop gfs.glm.db
# rm docker 
#sudo docker rm gfs.glm.db
# run docker 
#sudo docker run --name=gfs.glm.db -p 0.0.0.0:27016:27017 -v /home/bowen/git/Bohum/GFS/GFS.TMM/db/:/data/db -d mongo
echo start capture collection
python cc.py
