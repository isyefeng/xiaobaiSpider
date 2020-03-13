import urllib.request
import urllib.parse
import socket

urladdres = 'https://www.geekdigging.com/'

response = urllib.request.urlopen( urladdres )
#print(response.read().decode('utf-8'))
print(type(response))
print('响应码：'+str(response.version))
print(response.status)
print(response.getcode())
print(response.reason)
print(response.geturl())
print(response.getheader(name='Content-Type'))
print(response.getheaders())
print(response.info())
print(response.readline().decode('utf-8'))

post_data = bytes(urllib.parse.urlencode({'name': 'geekdigging', 'hello':'world'}), encoding='utf8')
print(post_data)
#response = urllib.request.urlopen('https://httpbin.org/post', data = post_data,timeout=2)
#print(response.read().decode('utf-8'))
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('请求超时')
    else:
        print(e)

