import requests
from bs4 import BeautifulSoup
root_url = "https://disp.cc/b/"
r = requests.get("https://disp.cc/b/PttHot")

soup = BeautifulSoup(r.text, "html.parser")  #parser解析器
# spans = soup.find_all("span", class_ = 'listTitle')
# for span in soup.find_all("span", class_ = 'listTitle'): find all寫法
	
# 	href = span.find("a").get("href") #或字典["href"]
# 	if href == "796-59l9":
# 		break

# 	url = root_url + href
# 	title = (span.text)
# 	print(f"{title}\n{url}")
#print([s.text for s in spans])

#CCS寫法
for span in soup.select("#list span.listTitle"):       #<--在css裡這是ID符號
	href = span.find("a").get("href") #或字典["href"]
	if href == "796-59l9":
		break

	url = root_url + href
	title = (span.text)
	print(f"{title}\n{url}")
