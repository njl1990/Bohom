# stop docker 
sudo docker stop gfs.tmm.db
sudo docker stop gfs.tmm.web
sudo docker stop gfs.tmm.dc
# rm docker 
sudo docker rm gfs.tmm.db
sudo docker rm gfs.tmm.web
sudo docker rm gfs.tmm.dc
# run docker 
# sudo docker run --net=tmm-net --name=gfs.tmm.db -v $PWD/db/:/data/db -p 0.0.0.0:27017:27017 -d mongo
sudo docker run --net=tmm-net --name=gfs.tmm.db -v /home/bowen/git/Bohom/GFS/GFS.TMM/db/:/data/db -d mongo
sudo docker run --net=tmm-net --name=gfs.tmm.web -v /home/bowen/git/Bohom/GFS/GFS.TMM/dev/:/home -p -i 0.0.0.0:8888:8888 -d bw:web.0.1 /bin/sh
sudo docker exec gfs.tmm.web "chmod 777 /home/run.sh"
sudo docker exec gfs.tmm.web "/home/run.sh"
#sudo docker run --net=tmm-net --name=gfs.tmm.dc -p 0.0.0.0:234:234 -d gfs-tmm:dc-0.1


