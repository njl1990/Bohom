#!/bin/sh
docker rmi bowen/gfs.glm.mkgif
docker build -t bowen/gfs.glm.mkgif .
mkdir -p /usr/local/mkgif
mkdir -p /usr/local/mkgif/images
mkdir -p /usr/local/mkgif/gif
cp run.sh /usr/local/mkgif/run.sh
chmod 777 /usr/local/mkgif/run.sh

