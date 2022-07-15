# zhihuspider
此项目的功能是爬取知乎热榜50条和评论，爬虫框架使用scrapy，数据存储使用mongo，可以下载下来做舆情分析  
# 说明
知乎爬取需要登录账号，本项目为了简便使用了cookie，将zhihu.py文件中的cookie更换成自己的cookie，注意使用字典形式

# 安装
git clone https://github.com/yaozp2n/zhihuspider.git 
所需运行环境,请看 ./requirements.txt  
数据库使用Mongodb存储，运行需要安装Mongodb，安装传送门  
https://www.mongodb.org/downloads  
如果仅仅作为测试不需要使用Mongodb，可以注释settings.py下对应行  
![178177505-3df70704-6bdf-4802-9ad7-93374516b80a](https://user-images.githubusercontent.com/24678542/179126432-399ec61b-caf5-4e79-b9e3-656bb6e8584d.png)  
本程序使用了代理池，在middlerwares.py文件加下填入代理池地址  
![178177813-eb0f4c2c-c9ca-460c-af97-dd75eeae50a4](https://user-images.githubusercontent.com/24678542/179126473-33365747-b0e5-4795-8223-61faf027b449.png)  
代理池的搭建，安装传送门  
http://blog.csdn.net/c406495762/article/details/72793480
# 运行  
以下命令统一运行在zhaopin/目录下，与scrapy.cfg文件同级目录  
scrapy crawl hot  
# 效果图  
![image](https://user-images.githubusercontent.com/24678542/179126809-63106b57-91d7-4145-a6c7-415145b5a6e9.png)
