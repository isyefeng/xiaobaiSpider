import http.cookiejar, urllib.request

#实例化cookiejar对象
cookie = http.cookiejar.CookieJar()
#使用HTTPCookeProcessor构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookie)
#构建opener
opener = urllib.request.build_opener(handler)
#发起请求
respose = opener.open('https://www.baidu.com/')
print(cookie)
for item in cookie:
	print(item.name+'='+item.value)
	
	
	
#将cookie保存为mozilla格式的文件
#实例化cookiejar对象
cookie = http.cookiejar.MozillaCookieJar('cookie_mozilla.txt')
#使用HTTPCookeProcessor构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookie)
#构建opener
opener = urllib.request.build_opener(handler)
#发起请求
respose = opener.open('https://www.baidu.com/')
cookie.save(ignore_discard=True, ignore_expires=True)


#将cookie保存为LWP格式的文件
#实例化cookiejar对象
cookie = http.cookiejar.LWPCookieJar('cookie_LWP.txt')
#使用HTTPCookeProcessor构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookie)
#构建opener
opener = urllib.request.build_opener(handler)
#发起请求
respose = opener.open('https://www.baidu.com/')
cookie.save(ignore_discard=True, ignore_expires=True)


#将cookie缓存文件（Mozilla格式）提取出来
#实例化cookiejar对象
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie_mozilla.txt',ignore_discard=True, ignore_expires=True)
#使用HTTPCookeProcessor构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookie)
#构建opener
opener = urllib.request.build_opener(handler)
#发起请求
respose = opener.open('https://www.baidu.com/')
print(respose.read().decode('utf-8'))





























