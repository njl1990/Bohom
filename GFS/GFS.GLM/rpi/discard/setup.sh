#!/bin/sh

APP_PATH=/usr/local/gfs/glm
IMAGE_PATH=/var/gfs/glm/images
INFO_PATH=/var/gfs/glm/info
GIF_PATH=/var/gfs/glm/gif

echo Create application path ...

echo create: $APP_PATH
mkdir -p $APP_PATH
echo create: $IMAGE_PATH
mkdir -p $IMAGE_PATH
echo create: $GIF_PATH
mkdir -p $GIF_PATH
echo create: $INFO_PATH
mkdir -p $INFO_PATH

# 1. build cc 
echo Install cc
echo Copy application files...
cp ./cc/cc.py $APP_PATH/cc.py

# build cc dependence
echo install application dependence...
#apt update
#apt install python3
#pip install Pillow
#pip install opencv-python

# 2. build save
echo Install save
echo Build docker images...
cd save
./build.sh
cd ..

# 2. build mkgif
echo Install mkgif
echo Build docker images...
docker stop gfs.glm.mkgif >/dev/null
docker rm gfs.glm.mkgif >/dev/null
docker rmi bowen/gfs.glm.mkgif >/dev/null
cd mkgif
./build.sh
cd ..

# 4.build runner 
echo Install appllication entrace...

sudo cp ./run.sh  $APP_PATH/run.sh
sudo cp ./stop.sh  $APP_PATH/stop.sh
sudo cp ./restart.sh  $APP_PATH/restart.sh

sudo chmod 777 $APP_PATH/run.sh
sudo chmod 777 $APP_PATH/stop.sh
sudo chmod 777 $APP_PATH/restart.sh

echo Success!