# GFS - Capture Log Moudle(GFS.GLM)
GLM  is a function moudle to implement the Capture Log, witch will collect image data from usb camra.

![glm](.\doc\img\glm.png)


## 1 TODO
- move mkgif to host, need to recode the setup scripts
- need to add the imageio into dependence

## 2 Dependence

* PIL

> pip install Pillow

* openvc

> pip install opencv-python 

## 3 Structure


### 3.1s Capture Log Database (CLDB)
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

​	Deploy Django+Python on the host server. Application name is **GLM**.

* When web service start up, image data will be download into web image path from database.

* Image data path：

  > .\clweb\dev\static\assets\images\glm\

#### 3.3.2.1 Overview.html




