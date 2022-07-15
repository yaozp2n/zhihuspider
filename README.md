# zhihuspider
此项目的功能是爬取知乎热榜50条和评论，爬虫框架使用scrapy，数据存储使用mongo，可以下载下来做舆情分析  
# 安装
git clone https://github.com/yaozp2n/zhihuspider.git 
所需运行环境,请看 ./requirements.txt  
数据库使用Mongodb存储，运行需要安装Mongodb，安装传送门  
https://www.mongodb.org/downloads  
如果仅仅作为测试不需要使用Mongodb，可以注释settings.py下对应行  

本程序使用了代理池，在middlerwares.py文件加下填入代理池地址  

代理池的搭建，安装传送门
http://blog.csdn.net/c406495762/article/details/72793480
