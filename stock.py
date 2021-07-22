import requests
from bs4 import BeautifulSoup

r = requests.get("https://tw.stock.yahoo.com/q/q?s=2605")
if r.status_code == requests.codes.ok:
	soup = BeautifulSoup(r.text, "html.parser")
	table = soup.find_all("table")[2]
	#print(table)

	price = table.find_all("td")[2]
	print(price.text)

	buy_price = price.find_next("td") #可以用price的標籤來取下一個
	print(buy_price.text)

	sell_price = table.find_all("td")[4]
	print(sell_price.text)