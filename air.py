from bs4 import BeautifulSoup
import requests
import pprint
import json
import re


r = requests.get("https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2021053016.json")
if r.status_code == requests.codes.ok:
	data = r.json()
	pprint.pprint(data)

	for d in data:
		name = d["Name"]
		if "AQI" not in name:
			continue
		elif "Name" == "鹿林山":
			continue
		result = re.search(r"(.+)\(AQI=(\d+)", name)
		site_name = result.group(1)
		aqi = result.group(2)
		print(site_name , aqi)