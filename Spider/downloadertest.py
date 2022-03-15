#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from http import cookiejar
import urllib3
 
url = "http://www.baidu.com"
response1 = urllib3.urlopen(url)
print ("第一种方法")
#获取状态码，200表示成功
print (response1.getcode())
#获取网页内容的长度
print (len(response1.read()))
 
print ("第二种方法")
request = urllib3.Request(url)
#模拟Mozilla浏览器进行爬虫
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib3.urlopen(request)
print (response2.getcode())
print (len(response2.read()))
 
print ("第三种方法")
cookie = cookiejar.CookieJar()
#加入urllib2处理cookie的能力
opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cookie))
urllib3.install_opener(opener)
response3 = urllib3.urlopen(url)
print (response3.getcode())
print (len(response3.read()))
print (cookie)