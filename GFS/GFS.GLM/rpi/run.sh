# RPI run.sh

APP_PATH=/usr/local/gfs/glm/
IMAGE_PATH=/var/gfs/glm/images
INFO_PATH=/var/gfs/glm/info
GIF_PATH=/var/gfs/glm/gif

#1.cc
echo start cc
nohup python /usr/local/gfs/glm/cc.py &

#2.save 
echo start save
docker stop gfs.glm.save >/dev/null
docker rm gfs.glm.save >/dev/null
docker run --name=gfs.glm.save -it -v $IMAGE_PATH:/images -v $INFO_PATH:/info bowen/gfs.glm.save 'python3' '/save.py'
#docker run --name=gfs.glm.save -d -v $IMAGE_PATH:/images -v $INFO_PATH:/info bowen/gfs.glm.save 'python3' '/save.py'

#3.mkgif
docker stop gfs.glm.mkgif >/dev/null
docker rm gfs.glm.mkgif >/dev/null
docker run --name=gfs.glm.mkgif -it -v $IMAGE_PATH:/images -v $GIF_PATH:/gif bowen/gfs.glm.mkgif 'python3' '/mkgif.py'
