# RPI run.sh

APP_PATH=/usr/local/gfs/glm/rpi

# startup capture collection
echo start capture collection
nohup python /usr/local/gfs/glm/rpi/src/cc.py &

# startup data update
echo start data update
nohup python /usr/local/gfs/glm/rpi/src/save.py &

