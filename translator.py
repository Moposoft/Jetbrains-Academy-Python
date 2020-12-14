from itertools import chain
import requests
from bs4 import BeautifulSoup
from sys import argv


def do_shit(fro, to, word):
    url = "https://context.reverso.net/translation/{}-{}/".format(fro, to)
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url + word, headers=headers)
    if r.status_code == 404:
        print("Sorry, unable to find {}".format(word))
        return
    file = open("{}.txt".format(word), 'a', encoding="utf-8")
    print("{} translation:".format(to))
    print("{} translation:".format(to), file=file)
    raw_contents = BeautifulSoup(r.content, 'html.parser')
    translations = raw_contents.find_all('a', {"class": 'translation'})
    sentences_src, sentences_target = \
        raw_contents.find_all('div', {"class": "src ltr"}), \
        raw_contents.find_all('div', {"class": ["trg ltr", "trg rtl arabic", "trg rtl"]})
    translation_list = [translation.get_text().strip().lower() for translation in translations]
    for n in range(len(translation_list)):
        print(translation_list[n])
        print(translation_list[n], file=file)
    print("{} example:".format(to))
    print("{} example:".format(to), file=file)
    sentence_list = [sentence.get_text().strip().lower() for sentence in
                     list(chain(*[sentence_pair for sentence_pair in zip(sentences_src, sentences_target)]))]
    s = "\n\n".join(("\n".join(j for j in sentence_list[i:i + 2]) for i in range(0, 10, 2)))
    print(s)
    print(s, file=file)
    file.close()


lan_from = argv[1]
lan_to = argv[2]
word = argv[3]

file = open("{}.txt".format(word), 'w', encoding="utf-8")
file.close()
lans = ["all", "arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
        "dutch", "polish", "portuguese", "romanian", "russian", "turkish"]
if lan_to not in lans:
    print("Sorry, the program doesn't support {}".format(lan_to))
elif lan_from not in lans:
    print("Sorry, the program doesn't support {}".format(lan_from))
elif lan_to != "all":
    do_shit(lan_from, lan_to, word)
else:
    for x in lans:
        if x != lan_from:
            do_shit(lan_from, x, word)

