import requests
from urllib.parse import urlparse
page = 0
# keyword = input("검색 내용 : ")


url = "https://api.github.com/search/repositories?q="+ keyword +"&sort=stars&order=desc"
result = requests.get(urlparse(url).geturl())
json_obj = result.json()

num = int(json_obj["total_count"])
print(num, "개 검색", sep='')
# print(len(json_obj)


for i in range(0, num):
    try:
        print(i+1,"번째")
        print (json_obj["items"][i]["owner"]["login"])
        print(json_obj["items"][i]["html_url"])
        print (json_obj["items"][i]["stargazers_count"], "\n")
    except:
        print("")


    # if json_obj["items"][i]["owner"]["login"] != []:
    #     print(json_obj["items"][0]["owner"]["login"])
    #     print(json_obj["items"][0]["owner"]["html_url"] + "\n")
    # else:
    #     json_obj["items"][0]["owner"]["html_url"] = ""









# print (json_obj["items"][0]["owner"])
#print(json_obj)

# del json_obj['items']

# print(json_obj)

# print(json_obj['items'])
#print(json_obj)

