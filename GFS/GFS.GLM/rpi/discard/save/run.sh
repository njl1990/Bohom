#!/bin/sh

APP_PATH=/usr/local/gfs/glm/
IMAGE_PATH=/var/gfs/glm/images
INFO_PATH=/var/gfs/glm/info
GIF_PATH=/var/gfs/glm/gif


docker stop gfs.glm.save
docker rm gfs.glm.save
docker run -it -v $IMAGE_PATH:/images -v $INFO_PATH:/info bowen/gfs.glm.save 'python3 /save.py'
#docker run -d -v $IMAGE_PATH:/images -v $INFO_PATH:/info bowen/gfs.glm.save 'python3 /save.py'