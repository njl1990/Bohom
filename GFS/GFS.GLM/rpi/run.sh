# RPI run.sh
APP_PATH=/usr/local/gfs/glm/

#1.cc
echo start cc
nohup python $APP_PATH/cc.py > $APP_PATH/cc.log & 
echo $! > $APP_PATH/cc_pid

#2.save 
echo start save
nohup python $APP_PATH/save.py > $APP_PATH/save.log & 
echo $! > $APP_PATH/save_pid

#3.mkgif
echo start mkgif
nohup python $APP_PATH/mkgif.py > $APP_PATH/mkgif.log & 
echo $! > $APP_PATH/mkgif_pid