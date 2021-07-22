import requests
from bs4 import BeautifulSoup
import pprint
import json

r = requests.get("https://chart.stock-ai.com/history?symbol=%5ETWII&resolution=D&from=1583051576&to=1622363636", verify = False)
if r.status_code == requests.codes.ok:
	data = r.json()

	zipped = zip(data["t"], data["o"], data["h"], data["l"], data["o"], data["v"])

	pprint.pprint(list(zipped))