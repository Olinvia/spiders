import requests
url = 'https://blog.csdn.net/shi_jiaye/article/details/119175407'
r = requests.get(url)
mycookies = r.cookies
# RequestsCookieJar转换字典
cookies_dict = requests.utils.dict_from_cookiejar(mycookies)
# 写入文件
f = open('cookies.txt', 'w', encoding='utf-8')
f.write(str(cookies_dict))
f.close()
# 读取文件
f = open('cookies.txt', 'r')
dict_value = f.read()
f.close()
# eval(dict_value)将字符串转换字典
print(eval(dict_value))
r = requests.get(url, cookies=eval(dict_value))
print(r.status_code)
