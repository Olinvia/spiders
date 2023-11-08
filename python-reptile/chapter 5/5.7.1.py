import urllib.request
import urllib.parse
url = 'https://movie.douban.com/'
data = {
    'value': 'true',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'}
# 数据处理
req = urllib.request.Request(url, headers=headers)
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.urlopen(req, data=data)
