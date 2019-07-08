FROM python
MAINTAINER bowen
RUN ["mkdir","-p","/images"]
RUN ["mkdir","-p","/gif" ]
COPY ./mkgif.py /mkgif.py
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","--upgrade","numpy"]
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","imageio"]

