#!/usr/bin/python3
from re import A
from urllib import response
import urllib.request
# from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import pymongo
import time
import datetime
from terminaltables import AsciiTable
import os

def downloadImg(url,savePath):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
        # 'cookie':'UM_distinctid=17f4f0836735fd-0a9cce3aad1793-7166786d-240480-17f4f0836744be; SINAGLOBAL=8619779136585.56.1646298412915; ALF=1678521659; SUB=_2AkMVc4a1f8NxqwJRmfocyGrgZYxzygDEieKjL3duJRMxHRl-yT_nqnIntRB6PvOoWmngxj0QFPKzLHzZXKUyg3YntvSz; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W50VGDZNmKX3qLsDEoOPG_k; _s_tentry=weibo.com; Apache=6978476875714.961.1647249952516; ULV=1647249952524:4:4:1:6978476875714.961.1647249952516:1646985509593'
    }  
    # data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
    request=urllib.request.Request(url,headers= header)   # 请求处理
    response=urllib.request.urlopen(request).read()      # 读取结果
    f = open(savePath, "wb")
    f.write(response)
    f.close()

def downloadPage(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
        # 'cookie':'UM_distinctid=17f4f0836735fd-0a9cce3aad1793-7166786d-240480-17f4f0836744be; SINAGLOBAL=8619779136585.56.1646298412915; ALF=1678521659; SUB=_2AkMVc4a1f8NxqwJRmfocyGrgZYxzygDEieKjL3duJRMxHRl-yT_nqnIntRB6PvOoWmngxj0QFPKzLHzZXKUyg3YntvSz; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W50VGDZNmKX3qLsDEoOPG_k; _s_tentry=weibo.com; Apache=6978476875714.961.1647249952516; ULV=1647249952524:4:4:1:6978476875714.961.1647249952516:1646985509593'
    }  
    # data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
    request=urllib.request.Request(url,headers= header)   # 请求处理
    response=urllib.request.urlopen(request).read()      # 读取结果
    # f = open("wbhotsearch.html", "wb")
    # f.write(reponse)
    # f.close()
    return response
html = downloadPage('https://www.smh.com.au/politics/federal/morrison-gets-personal-as-he-puts-down-the-albanese-glow-up-20220315-p5a4t7.html')
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
title = soup.h1.string
print(title)
author = soup.select('span[data-testid="byline"]')[0].string
print(author)
# for i in soup.body.strings:
#     print(i)
contents = soup.select('div[data-testid="body-content"]')
# =========================================
root = 'articles'
date = str(datetime.date.today())
if not os.path.exists(root):
    os.mkdir(root)
if not os.path.exists(root + '\\'+ date):
    os.mkdir(root + '\\'+ date)
if not os.path.exists(root + '\\'+ date+ '\\' + title ):
    os.mkdir(root + '\\'+ date+ '\\' + title )
dir = root + '\\'+ date+ '\\' + title+'\\'
if os.path.exists(dir+'\\'+'content.txt'):
    os.remove(dir+'\\'+'content.txt')
fs = open(dir+'\\'+'content.txt','ab')
#=========================================
fs.write(('标题：'+ title+'\n') .encode('utf-8'))
fs.write(('作者：'+ author+'\n') .encode('utf-8'))
for content in contents:
    for text in content.strings:
        fs.write((text+'\n') .encode('utf-8'))

imgIndex = 0
for content in contents:
    imgs =  content.select('img')
    for img in imgs:
        print(img['src'])
        downloadImg(img['src'], dir+'\\'+ str(imgIndex) +'.png')
        imgIndex = imgIndex + 1
fs.close()
