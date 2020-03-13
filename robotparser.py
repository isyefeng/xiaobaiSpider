import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.cnblogs.com/robots.txt') #设置robots.txt连接，也可以在创建对象时指定
rp.read()  #读取和解析文件
#can_fetch()方法查询是否可以爬取
print(rp.can_fetch('*','https://i.cnblogs.com/EditPosts.aspx?postid=9170312&update=1')) #坚持链接是否可以被抓取
