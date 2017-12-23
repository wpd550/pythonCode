
import  urllib.request
import  urllib.parse
import  http.cookiejar

home ="http://www.mmjpg.com"
#url = "http://img.mmjpg.com/2017/1202/5.jpg"
# header= "User-Agent:Mozilla"
# req = urllib.request.Request(url)
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063')
# req.add_header('Refere','http://www.mmjpg.com/')
# req.add_header('Connection','keep-alive')
# cjar =http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# urllib.request.install_opener(opener)
# file =opener.open(req)
#reqq= urllib.request.urlopen(url)
#data =reqq.read();


cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)


url='http://img.mmjpg.com/2017/1206/1.jpg'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063')
req.add_header('Refere','http://www.mmjpg.com/')
req.add_header('Connection',' Keep-Alive')
#urllib.request.urlopen(home)
data = urllib.request.urlopen(req).read()

path = open("G:/test02.jpg","wb")

path.write(data)
path.close()