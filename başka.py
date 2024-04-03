import requests
from bs4 import BeautifulSoup

url = "https://rapidvid.net/vod/v1xf59086cb"

# Web sayfasını indirin
response = requests.get(url)
content = response.content

# BeautifulSoup ile sayfa içeriğini işleyin
soup = BeautifulSoup(content, "html.parser")
pagecontent = soup.prettify()

# Videoyu içeren elementi bulun
print(pagecontent)

