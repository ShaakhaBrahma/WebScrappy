import re, urllib, datetime
from datetime import datetime
from urllib.request import Request, urlopen
url = 'https://hebbarskitchen.com/'
try : req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
except urllib.error.URLError as e:
    print(e.reason)
start= datetime.now()
stime = float((start.strftime('%S.%f')))
web_byte = urlopen(req).read()
end = datetime.now()
etime = float((end.strftime('%S.%f')))
webpage = web_byte.decode('utf-8')
scripts = re.findall('<script\stype=\'application/ld\+json\'.+>({.*?})</script>?', webpage)
name = re.findall('"name":"(.*?)",?', scripts[0])
print('Extracted structured data:', scripts)
print('All titles:', name)
print('response time:%f ms'% ((etime-stime)*1000))
print('status code:200 ok')



