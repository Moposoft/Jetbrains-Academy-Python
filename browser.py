# write your code here
from sys import argv
from os import mkdir, path
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore
HEADERS = {'user-agent': 'Mozilla/5.0'}


def valid(url):
    return len(url.split(".")) > 1


def page_to_file(url):
    print(url)
    file = url.split(".")[0]
    #if url[0:12] != "https://www.":
    #    url = "https://www." + url
    if url[0:8] != "https://":
        url = "https://" + url
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        file = argv[1] + "/" + file
        soup = BeautifulSoup(r.content, features="html.parser")
        soup.find_all(['a', 'p', 'ul', 'ol', 'li'])
        print(Fore.BLUE + soup.get_text())
        with open(file, 'w', encoding="UTF-8") as f:
            print(Fore.BLUE + soup.get_text(), file=f)
    else:
        print("PROBLEMA")


d = deque()
while True:
    print(d)
    url = input()
    if url == "exit":
        exit()
    if url == "back":
        if len(d) > 0:
            print(d[0])
            d.pop()
        else:
            continue
    if not path.exists(argv[1]):
        mkdir(argv[1])
    if valid(url):
        d.append(url)
        page_to_file(url)
    else:
        print("Error: Incorrect URL")
