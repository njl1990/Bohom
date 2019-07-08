FROM python
MAINTAINER bowen
RUN ["mkdir","-p","/images"]
COPY save.py /save.py
RUN ["pip","install","-i","http://mirrors.aliyun.com/pypi/simple/","--trusted-host","mirrors.aliyun.com","--upgrade","pymongo"]

