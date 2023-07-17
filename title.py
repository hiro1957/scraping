import requests
from bs4 import BeautifulSoup
 
url = "https://yahoo.co.jp"
 
r = requests.get(url)
 
soup = BeautifulSoup(r.content, "html.parser")

 
print(soup.select("title"))
