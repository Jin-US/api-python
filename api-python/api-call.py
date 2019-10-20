import requests
from urllib.parse import urlparse

keyword = input("원하는 검색 결과 : ")
url = "https://api.github.com/search/repositories?q="+ keyword

result = requests.get(urlparse(url).geturl())

json_obj = result.json()


num = json_obj["total_count"]

print(num)

for i in range(0,num):
    print (json_obj["items"][i]["owner"]["login"])
    print (json_obj["items"][i]["owner"]["html_url"]+"\n")
    if json_obj["items"][i]["owner"]["login"] != []:
        print(json_obj["items"][0]["owner"]["login"])
        print(json_obj["items"][0]["owner"]["html_url"] + "\n")
    else:
        json_obj["items"][0]["owner"]["html_url"] = ""









# print (json_obj["items"][0]["owner"])
#print(json_obj)

# del json_obj['items']

# print(json_obj)

# print(json_obj['items'])
#print(json_obj)

