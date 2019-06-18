# install gfs.glm

# build path
APP_PATH=/usr/local/gfs/glm/rpi
sudo mkdir -p $APP_PATH/src
sudo mkdir -p $APP_PATH/shell

echo copy application files...
# install files 
sudo cp ./cc/cc.py $APP_PATH/src/cc.py
sudo cp ./cc/save.py $APP_PATH/src/save.py
sudo cp ./imgsrv/img.py $APP_PATH/src/img.py
sudo cp ./imgsrv/img.py $APP_PATH/src/img.py
sudo cp ./run.sh  $APP_PATH/run.sh
sudo cp ./stop.sh  $APP_PATH/stop.sh
sudo cp ./restart.sh  $APP_PATH/restart.sh

sudo chmod 777 $APP_PATH/run.sh
sudo chmod 777 $APP_PATH/stop.sh
sudo chmod 777 $APP_PATH/restart.sh

echo install application dependence...
#install module
sudo apt update
sudo apt install python3
#sudo apt install docker
#pip install Pillow
#pip install opencv-python

echo Done
