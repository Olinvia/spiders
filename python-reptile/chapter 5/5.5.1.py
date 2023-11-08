import urllib.request
from http import cookiejar
filename = 'cookie.txt'
# MozillaCookieJar保存cookie
cookie = cookiejar.MozillaCookieJar(filename)
# HTTPCookieProcessor创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建自定义opener
opener = urllib.request.build_opener(handler)
# open方法打开网页
response = opener.open('https://blog.csdn.net/shi_jiaye/article/details/119175407')
# 保存cookie文件
cookie.save()
