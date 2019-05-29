# stop docker 
sudo docker stop gfs.tmm.db
sudo docker stop gfs.tmm.web
sudo docker stop gfs.tmm.dc
# rm docker 
sudo docker rm gfs.tmm.db
sudo docker rm gfs.tmm.web
sudo docker rm gfs.tmm.dc
# run docker 
sudo docker run --name=gfs.tmm.db -v $PWD/db/:/data/db -p 0.0.0.0:27017:27017 -d mongo
sudo docker run --name=gfs.tmm.web -v $PWD/dev/:/source -p 0.0.0.0:8888:8888 -d gfs-tmm:web-0.1
sudo docker exec gfs.tmm.web "chmod 777 /source/run.sh"
sudo docker exec gfs.tmm.web "/source/run.sh"
#sudo docker run --name=gfs.tmm.dc -p 0.0.0.0:234:234 -d gfs-tmm:dc-0.1


