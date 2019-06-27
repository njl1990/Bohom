#!/bin/sh
docker stop gfs.glm.mkgif
docker rm gfs.glm.mkgif
docker run --name=gfs.glm.mkgif -it -v /usr/local/gfs/glm/images:/images -v /usr/local/gfs/glm/gif:/gif bowen/gfs.glm.mkgif 'python3' 'mkgif.py'
