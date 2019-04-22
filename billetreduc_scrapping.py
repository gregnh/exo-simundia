import urllib3
import json
import sys

sys.path.append("./module")
import functions as f

data = {}
spectacle_counter = 1
http = urllib3.PoolManager()

page_1 = "liste.htm"
data, spectacle_counter = f.get_infos(page_1, http, data, spectacle_counter)


soup = f.parsing_html_page("https://www.billetreduc.com/one-man-show/R/3/{}".format(page_1),
                           http)
# # get other pages tags
other_pages_tags = set(soup.find_all("a", {"class": "page-number-link"}))
for a in other_pages_tags:
    page_url = a["href"]
    data, spectacle_counter = f.get_infos(page_url, http, data, spectacle_counter)
    print(len(data), spectacle_counter - 1)

# Saving json
with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
