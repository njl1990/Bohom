# stop docker 
sudo docker stop gfs.glm.db
sudo docker stop gfs.glm.web
#sudo docker stop gfs.glm.dc

# rm docker 
sudo docker rm gfs.glm.db
sudo docker rm gfs.glm.web
#sudo docker rm gfs.glm.dc

# run docker 
sudo docker run  --name=gfs.glm.db -p 0.0.0.0:27016:27017 -v /home/bowen/git/Bohom/GFS/GFS.GLM/db/:/data/db -d mongo
sudo docker run  --name=gfs.glm.web --link=gfs.glm.db:db  -v /home/bowen/git/Bohom/GFS/GFS.GLM/dev/clweb/dev:/home -id -p 0.0.0.0:8889:8888 bw:web.0.1 '/bin/sh'

#sudo docker exec -id --privileged  gfs.glm.web '/bin/sh' '/home/run.sh'
sudo docker exec -it --privileged gfs.glm.web 'bin/sh'
#sudo docker run --net=GLM-net --name=gfs.glm.dc -p 0.0.0.0:234:234 -d gfs-GLM:dc-0.1


