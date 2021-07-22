import requests
from bs4 import BeautifulSoup
from collections import Counter

#r = requests.get(https://www.dcard.tw/f/2019_ncov/p/236052352/{}.format)
data = []
n = 0
while True:
	r= requests.get("https://www.dcard.tw/f/2019_ncov/p/236052352/b/", n)
	soup = BeautifulSoup(r.text, "html.parser")
	spans = soup.find("div", class_ = "dbFiwE")
	
