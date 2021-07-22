import requests
from bs4 import BeautifulSoup
import pandas as pd


r = requests.get("https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx")
if r.status_code == requests.codes.ok:
	soup = BeautifulSoup(r.text, "lxml")
	#print(soup.prettify())
	tables = soup.find_all("table", attrs= {"cellpadding" : "2"})
	#print(tables[0])

	for table in tables:
		trs = table.find_all("tr")
		for tr in trs:
			date, value, prive = [td.text for td in tr.find_all("td")] #因為有三個東西可以直接這樣寫
			if date == "日期":
				continue
			data.append([date, value, prive])

df = pd.DataFrame(data, columns=["日期", "買賣超金額", "台指期"])
#df.to_csv("big_eight.csv")
#df.to_excel("big_eight.xlsx")
df.to_html("big_eight.html")
#print(data)