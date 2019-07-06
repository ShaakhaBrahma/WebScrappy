import re
from urllib.request import Request, urlopen
url = 'https://hebbarskitchen.com/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
scripts = re.findall('<script\stype=\'application/ld\+json\'.+>({.*?})</script>?', webpage)
print(scripts)


