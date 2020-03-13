from urllib import request,error

#urllib错误
try:
	response = request.urlopen('https://www.geekdigging.com/aa')
except error.URLError as e:
	print(e.reason)		#返回错误原因
	print(e.code)		#返回错误代码
	print(e.headers)	#返回请求头
	
try:
	response = request.urlopen('https://www.geekdigging.com/',timeout=0.01)
except error.URLError as e:
	print(e.reason)

try:
	response = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
	print(e.reason)		#返回错误原因
	print(e.code)		#返回错误代码
	print(e.headers)	#返回请求头
	