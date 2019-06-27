#!/bin/sh
docker stop gfs.glm.mkgif
docker rm gfs.glm.mkgif
docker rmi bowen/gfs.glm.mkgif
docker build -t bowen/gfs.glm.mkgif .

