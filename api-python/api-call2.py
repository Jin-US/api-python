import requests
from urllib.parse import urlparse
import sys
index = 0
page = 1
keyword = input("검색 내용 : ")

def search(index):
    temp = str(page)
    url = "https://api.github.com/search/repositories?q=" + keyword +"&sort=stars&order=desc&page=" + temp
    result = requests.get(urlparse(url).geturl())
    json_obj = result.json()

    num = int(json_obj["total_count"])
    print(num, "개 검색", sep='')

    for i in range(0, index+30):
        try:
            print(i+1+(page*30-30),"번째")
            print (json_obj["items"][i]["owner"]["login"])
            print(json_obj["items"][i]["html_url"])
            print (json_obj["items"][i]["stargazers_count"], "\n")
        except:
            print("")


while(1):
    search(index)
    print("Next 입력시 다음 페이지")
    print(page, "Page")
    A = sys.stdin.readline().split()
    if(A == "Next") | (index == 0):
        index = index
        page = page+1
    else:
        break
