#!/usr/bin/python3
from urllib import response
import urllib.request
# from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import pymongo
import time
import datetime
from terminaltables import AsciiTable

# -------------------------------------------
# -------------------------------------------
# 字体色     |       背景色     |      颜色描述
# -------------------------------------------
# 30        |        40       |       黑色
# 31        |        41       |       红色
# 32        |        42       |       绿色
# 33        |        43       |       黃色
# 34        |        44       |       蓝色
# 35        |        45       |       紫红色
# 36        |        46       |       青蓝色
# 37        |        47       |       白色
# -------------------------------------------
# -------------------------------
# 显示方式     |      效果
# -------------------------------
# 0           |     终端默认设置
# 1           |     高亮显示
# 4           |     使用下划线
# 5           |     闪烁
# 7           |     反白显示
# 8           |     不可见
# -------------------------------


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["spider"]
weibohscol = db["weibohs"]
# 下载网页
def downloadPage():
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
        'cookie':'UM_distinctid=17f4f0836735fd-0a9cce3aad1793-7166786d-240480-17f4f0836744be; SINAGLOBAL=8619779136585.56.1646298412915; ALF=1678521659; SUB=_2AkMVc4a1f8NxqwJRmfocyGrgZYxzygDEieKjL3duJRMxHRl-yT_nqnIntRB6PvOoWmngxj0QFPKzLHzZXKUyg3YntvSz; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W50VGDZNmKX3qLsDEoOPG_k; _s_tentry=weibo.com; Apache=6978476875714.961.1647249952516; ULV=1647249952524:4:4:1:6978476875714.961.1647249952516:1646985509593'
    }  
    # data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
    request=urllib.request.Request(url,headers= header)   # 请求处理
    response=urllib.request.urlopen(request).read()      # 读取结果
    # f = open("wbhotsearch.html", "wb")
    # f.write(reponse)
    # f.close()
    return response


def catchHots(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    table_data = [ ['标题','状态']]
    for td02a in soup.select('.td-02 > a'):
        query = { "title":td02a.string ,"createtime": { "$gte": datetime.datetime.combine(datetime.date.today(),datetime.datetime.min.time())} }
        doc_count = weibohscol.count_documents(query)
        if doc_count == 0:
            unencode_url ='https://s.weibo.com' + urllib.request.unquote(td02a['href'])    # 解码
            item = {'url': unencode_url,'title':td02a.string,'createtime':datetime.datetime.today()}
            x = weibohscol.insert_one(item)  
            table_data.append([td02a.string,'\033[0;32;40m【收录成功】\033[0m'])
        else:
            table_data.append([td02a.string,'\033[0;31;40m【已存在】\033[0m'])
    return table_data

table = AsciiTable(catchHots(downloadPage()))
print(table.table)
