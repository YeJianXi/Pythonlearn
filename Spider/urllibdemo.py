import urllib.request
# from urllib.request import urlopen
from urllib.parse import urlparse



# myURL = urllib.request.urlopen("https://www.runoob.com/")
# print(myURL.getcode())
# lines = myURL.readlines()
# print(type(lines))
# for line in lines:
    # print(line)



# try:
#     myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
# except urllib.error.HTTPError as e:
#     if e.code == 404:
#         print(404)   # 404

# myURL = urlopen("https://www.baidu.com/")
# f = open("runoob_urllib_test.html", "wb")
# content = myURL.read()  # 读取网页内容
# f.write(content)
# f.close()


# encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
# print(encode_url)

# unencode_url = urllib.request.unquote(encode_url)    # 解码
# print(unencode_url)


# url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
# keyword = 'Python 教程'
# key_code = urllib.request.quote(keyword)  # 对请求进行编码
# url_all = url+key_code
# header = {
#     'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }   #头部信息
# request = urllib.request.Request(url_all,headers=header)
# reponse = urllib.request.urlopen(request).read()

# fh = open("./urllib_test_runoob_search.html","wb")    # 将文件写入到当前目录中
# fh.write(reponse)
# fh.close()

# url = 'https://www.runoob.com/try/py3/py3_urllib_test.php'  # 提交到表单页面
# data = {'name':'RUNOOB', 'tag' : '菜鸟教程'}   # 提交数据
# header = {
#     'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }   #头部信息
# data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
# request=urllib.request.Request(url, data, header)   # 请求处理
# reponse=urllib.request.urlopen(request).read()      # 读取结果

# fh = open("./urllib_test_post_runoob.html","wb")    # 将文件写入到当前目录中
# fh.write(reponse)
# fh.close()





# myURL1 = urllib.request.urlopen("https://www.runoob.com/")
# print(myURL1.getcode())   # 200

# try:
#     myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
# except urllib.error.HTTPError as e:
#     if e.code == 404:
#         print(404)   # 404




# o = urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
# print(o)