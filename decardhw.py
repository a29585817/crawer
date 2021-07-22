import requests
from bs4 import BeautifulSoup
import time

def crawl(floor):
    try:
        r = requests.get("https://www.dcard.tw/f/2019_ncov/p/236143798/b/{}".format(floor))
        soup = BeautifulSoup(r.text, "html.parser")
        name = soup.find("div", class_ = "sc-7fxob4-4 dbFiwE")
        comment = soup.find("div", class_ = "phqjxq-0 fQNVmg")  
        name = name.text
        comment = comment.text
        return name , comment 
    except:
        print("資料找完了")

n = 1
sum = 0
round = 0
people = []
total = []

starttime = time.time()

while True:
    data = crawl(n)
    if not data:
        break
    sum += len(data[1])
    people.append(data[0])
    round += 1
    n += 1


for i in set(people):
    total.append(people.count(i))
final_list = list(zip(people, total))


endtime = time.time()
spend = endtime - starttime

print(sorted(final_list, key = lambda final_list:final_list[1]))
result = sum / round
print("總共有", round, "人留言")
print("一個人平均留", result, "個字")
print("總共花了" , spend , "秒")
