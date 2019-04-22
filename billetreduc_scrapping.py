import urllib3
from bs4 import BeautifulSoup
import json
import sys

sys.path.append("./module")
import functions as f

data = {}
spectacle_counter = 1
http = urllib3.PoolManager()

page_1 = "liste.htm"
response = http.request('GET',
                        "https://www.billetreduc.com/one-man-show/R/3/{}".format(page_1))
soup = BeautifulSoup(response.data)

titles = soup.find_all("a", {"class": "head"})
descriptions = soup.find_all("div", {"class": "libellepreliste"})
data, spectacle_counter = f.add_infos(data, titles, descriptions, spectacle_counter)


# get other pages url
for a in set(soup.find_all("a", {"class": "page-number-link"})):
    page = a["href"]

    response = http.request('GET',
                            "https://www.billetreduc.com/one-man-show/R/3/{}".format(page))
    soup = BeautifulSoup(response.data)
    titles = soup.find_all("a", {"class": "head"})
    descriptions = soup.find_all("div", {"class": "libellepreliste"})
    data, spectacle_counter = f.add_infos(data, titles, descriptions, spectacle_counter)
    print(len(data), spectacle_counter - 1)

# Saving json
with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
