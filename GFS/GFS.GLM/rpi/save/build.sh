#!/bin/sh

APP_PATH=/usr/local/gfs/glm/
IMAGE_PATH=/var/gfs/glm/images
INFO_PATH=/var/gfs/glm/info
GIF_PATH=/var/gfs/glm/gif


docker stop gfs.glm.save
docker rm gfs.glm.save
docker rmi bowen/gfs.glm.save
docker build -t bowen/gfs.glm.save .
