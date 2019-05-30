# GFS - Capture Log Moudle(GFS.GLM)
GLM 实现图像日志功能，运行中能够驱动摄像头定时采集图像，并存储入库。


## Depend

### PIL
pip install Pillow

### openvc
pip install opencv-python 

## Structure

### Capture Collector (CC)
部署运行在宿主机，直接驱动硬件
输入：硬件
输出：CLDB

### Capture Log Database (CLDB)
部署运行在Docker容器
输入：CC

### Capture Log Web (CLweb)
部署运行在Docker容器
输入：CLDB
输出：web

### Log Process (CP)
部署运行在Docker容器
输入：CLDB
输出：CLDB
