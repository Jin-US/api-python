import requests
from urllib.parse import urlparse

keyword = input("원하는 검색 결과 : ")
url = "https://api.github.com/search/repositories?q="+ keyword

result = requests.get(urlparse(url).geturl())

json_obj = result.json()

print(json_obj['items'])










#print(json_obj)

# del json_obj['items']

# print(json_obj)

# print(json_obj['items'])
#print(json_obj)

