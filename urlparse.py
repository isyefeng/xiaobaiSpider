from urllib.parse import urlparse, urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin

result = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse')
print(type(result))
print(result)

print(result.path)		#
print(result[1])		#通过索引的方式读取

#url构造
params = ('https', 'www.geekdigging.com', 'index.html', 'people', 'a=1', 'geekdigging')
print(urlunparse(params))

#urlsplit  
#urlsplit与urlparse很像，但是他不单独解析params，而是直接包含在了path中
result_urlsplit = urlsplit("https://www.geekdigging.com/index.html;people?a=1#geekdigging")
print(type(result_urlsplit))
print(result_urlsplit)

#构造url urlsplit方法
params_urlunsplit = ('https', 'www.geekdigging.com', 'index.html;people', 'a=1', 'geekdigging')
print(urlunsplit(params_urlunsplit))

print('/******************************************************\r\nurljoin\r\n********************************************************/')
print(urljoin("https://www.geekdigging.com/", "index.html"))
print(urljoin("https://www.geekdigging.com/", "https://www.geekdigging.com/index.html"))
print(urljoin("https://www.geekdigging.com/", "?a=aa"))
print(urljoin("https://www.geekdigging.com/#geekdigging", "https://docs.python.org/zh-cn/3.7/library/urllib.parse.html"))
