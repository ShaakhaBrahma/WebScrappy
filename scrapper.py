import re, urllib
from urllib.request import Request, urlopen
url = 'https://hebbarskitchen.com/'
start=
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print(at.status)
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
scripts = re.findall('<script\stype=\'application/ld\+json\'.+>({.*?})</script>?', webpage)
name = re.findall('"name":"(.*?)",?',scripts[0])
print('Extracted structured data:',scripts)
print('All titles in it:',name,at.info())



