# build path
APP_PATH=/usr/local/gfs/glm/host
sudo mkdir -p $APP_PATH/src
sudo mkdir -p $APP_PATH/db


echo copy application files...
sudo cp -r ./clweb $APP_PATH/src/clweb
sido cp ./imgsrv $APP_PATH/src/img.py
echo Done