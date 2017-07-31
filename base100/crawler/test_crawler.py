import urllib.request
import chardet

data = urllib.request.urlopen('http://www.dangdang.com/').read()

print(data.decode('gbk'))
print(chardet.detect(data))