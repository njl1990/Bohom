APP_PATH=/usr/local/gfs/glm/host

# stop docker
sudo docker stop gfs.glm.db
sudo docker stop gfs.glm.web
sudo docker stop gfs.glm.dc

# rm docker 
sudo docker rm gfs.glm.db
sudo docker rm gfs.glm.web
sudo docker rm gfs.glm.dc

# run docker 
sudo docker run  --name=gfs.glm.db -p 0.0.0.0:27016:27017 -v $APP_PATH/db/:/data/db -d mongo
sudo docker run  --name=gfs.glm.web --link=gfs.glm.db:db  -v $APP_PATH/src/dev:/home -id -p 0.0.0.0:8889:8888 bw:web.0.1 '/bin/sh'
sudo docker run  --name=gfs.glm.dc --link=gfs.glm.db:db -v $APP_PATH/src/clweb/dev/static/assets/images/glm/:/img pymongo -v $APP_PATH/src/:/home pymongo '/bin/sh'

sudo docker exec -id --privileged gfs.glm.web 'bin/sh'
sudo docker exec -id --privileged gfs.glm.dc 'bin/sh' '/home/run.sh'
#sudo docker run --net=GLM-net --name=gfs.glm.dc -p 0.0.0.0:234:234 -d gfs-GLM:dc-0.1
#sudo docker exec -id --privileged  gfs.glm.web '/bin/sh' '/home/run.sh'