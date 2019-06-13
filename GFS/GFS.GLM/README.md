# GFS - Capture Log Moudle(GFS.GLM)
GLM  is a function moudle to implement the Capture Log, witch will collect image data from usb camra.


## 1 Schedule
#### 12/6 depart the cc module and data save module

When I departed the old cc module, the RPI alway notice an error : 'can't import pymongo'. 

Solution: 

use

> python save.py

instead **sudo python **

## 2 Dependence

* PIL

> pip install Pillow

* openvc

> pip install opencv-python 

## 3 Structure

### 3.1 Capture Collector (CC)
* Deploy on the RPI (raspberry pi)

* buid.sh

  ​	Iinit database

* run.sh/run.bat

  > python cc.py

  running cc main function

  * Use an USB camera collecting image.

  * Save image as file at local path:

    > ./img

### 3.2 Capture Log Database (CLDB)
* Deploy on the host server.

* Running as a docker container named : **gfs.glm.db**

* port : **27016**

* data path : **/home/bowen/git/Bohom/GFS/GFS.GLM/db/**

* container data path: **/data/db**

  > sudo docker run --name=gfs.glm.db -p 0.0.0.0:27016:27017 -v /home/bowen/git/Bohom/GFS/GFS.GLM/db/:/data/db -d mongo

### 3.3 Capture Log Web (CLweb)

- Deploy on the host server.
- Running as a docker container named : **gfs.glm.web**
- Running Python3+Django Image
- Function:  show images and gif

### 3.3.1 Log Process (CP)

* Deploy on the host server.
* Running in the container : **gfs.glm.web**

### 3.3.2 CLweb

#### 3.3.2.1 Overview.html



