# https://github.com/fawazahmed0/quran-api

import requests
from pprint import pprint as print
 
sura = 1
oyat = 2


tafsir='uzb-muhammadsodikmu'

url_sura=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
url_oyat=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"

s = requests.get(url_sura)
r = requests.get(url_oyat)
# print(r.status_code) //200 or 404
res = r.json()
res2 = s.json()

# print(res)