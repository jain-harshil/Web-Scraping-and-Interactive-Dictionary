from bs4 import BeautifulSoup
import requests
import sys
import re
#all required libraries have been loaded
t = str(input())
r = requests.get("http://pythonslides.review/Slides/Lec0"+t)
#all content from the slides loaded
c = r.content
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
soup = BeautifulSoup(c,"html.parser")
k1 = soup.find_all(textarea)
d=(str(k1[0]).translate(non_bmp_map))
p = r"```python(.*|\n)+?```"
#Regular expression used to find the snippets
s = re.findall(p,d)
print(s)
