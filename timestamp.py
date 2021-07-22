import requests
from bs4 import BeautifulSoup

data = {"timestamp" : "2143223" , "Submit" : "Convert"}
r = requests.get("https://www.unixtimestamp.com/index.php", data = data)
if r.status_code == requests.codes.ok:
	soup = BeautifulSoup(r.text, "html.parser")
	print(soup.prettify())