FROM python
MAINTAINER bowen
RUN ["mkdir","-p","/usr/local/mkgif"]
RUN ["mkdir","-p","/images"]
RUN ["mkdir","-p","/gif" ]
COPY ./mkgif.py /usr/mkgif/mkgif.py
RUN ["pip","install","imageio"]
