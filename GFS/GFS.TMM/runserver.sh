# rm docker 
sudo docker rm gfs.tmm.db
sudo docker rm gfs.tmm.web
sudo docker rm gfs.tmm.dc
# run docker 
sudo docker run --name=gfs.tmm.db -v $PWD/db/:/db/ -p 0.0.0.0:1234:1234 -d gfs-tmm:db-0.1
sudo docker run --name=gfs.tmm.web -p 0.0.0.0:8888:8888 -d gfs-tmm:web-0.1
sudo docker run --name=gfs.tmm.dc -p 0.0.0.0:234:234 -d gfs-tmm:dc-0.1


