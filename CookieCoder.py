from urllib import  request
from  http import cookiejar
home ="http://www.mmjpg.com"
cjar = cookiejar.CookieJar()
handle= request.HTTPCookieProcessor(cjar)
opener = request.build_opener(handle)
request.install_opener(opener)



header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"deflate",
    "Connection": "keep-alive",
    "Referer":" http://www.mmjpg.com/mm/",
    "Upgrade-Insecure-Requests": "1"
}
image = 'http://img.mmjpg.com/2017/1202/5.jpg'
req = request.Request(url=image, headers=header)
#data =request.urlopen(req)
resp = request.urlopen(req)
data=resp.read()

path =open("G:/02.jpg",'wb')
path.write(data)
path.close()

print(cjar)