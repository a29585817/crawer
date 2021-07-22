from bs4 import BeautifulSoup
import requests
import pprint
import json
import re


r = requests.get("https://www.wantgoo.com/stock/2420/profitability/roe-roa")
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find_all("tr style")
print(table)