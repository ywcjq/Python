#/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import re
url = r'http://www.baidu.com'
file='index.htm'
wb= urlopen(url).read().decode()
#par=r'''href=(?P<quoto>['"])([^\1]+?)(?P=quoto)'''
#p=re.compile(par)
#urllist= p.findall(wb)
#result=['<p>' + i[1] + '</p>' for i in urllist]

#with open(file,'w') as f:
#  f.writelines(result)

soup= BeautifulSoup(wb)
alinks= soup.select('a')
for link in alinks:
  if '://' not in like:
    if link['href'][0]=='/':
      quoto=''
    else:
      quoto='/'
    link['href']=url + quoto +link['href']
with open(file,'w') as f:
  f.writelines(alinks)
  
print('Done.')