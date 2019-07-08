APP_PATH=/usr/local/gfs/glm/
IMAGE_PATH=/var/gfs/glm/images
INFO_PATH=/var/gfs/glm/info
GIF_PATH=/var/gfs/glm/gif


docker stop gfs.glm.mkgif >/dev/null
docker rm gfs.glm.mkgif >/dev/null
docker run --name=gfs.glm.mkgif -it -v $IMAGE_PATH:/images -v $GIF_PATH:/gif bowen/gfs.glm.mkgif 'python3' '/mkgif.py'
