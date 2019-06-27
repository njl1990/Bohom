#!/bin/sh
docker stop gfs.glm.save
docker rm gfs.glm.save
docker rmi bowen/gfs.glm.save
docker build -t bowen/gfs.glm.save .

