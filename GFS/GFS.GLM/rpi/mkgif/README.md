# mkgif - make gif file(GFS.GLM.MKGIF)
This program make image files into gif file.

# Guild
#### step1
download ***./build.sh***

#### step2
running build script
> ./build.sh

#### step3
startup applications

# Download

# Issues

* coding: Dockfile
make sure that the docker container could build on the rpi enviroment.

* coding: build.sh
1. stop,remove the container
2. remvoe the image
3. docker build the Dockerfile

* coding: run.sh
restart docker container

* coding: mkgif.py
design the input and output path
in: /images
out: /gif