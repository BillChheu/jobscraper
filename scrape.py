import requests
from bs4 import BeautifulSoup
import re

prev = ""
# initalization of comment to be different than prev for first run
comments = "comments"
p = 1

while (prev != comments):

    page = requests.get("https://news.ycombinator.com/item?id=27699704&p=%d" % p)
    print("Page %d" % p)
    p += 1

    soup = BeautifulSoup(page.text, "html.parser")

    prev = comments
    comments = soup.find_all(class_="comment")

    for x in range(len(comments)):
        # regex to find all instances of keywords of entry level positions
        entryLevelPosting = comments[x].find_all(text=re.compile("junior|^associate|^entry|^Jr|^entry|entry-", flags=re.IGNORECASE))
        
        if (entryLevelPosting):
            print(comments[x].get_text('\n'))
        
        


#print(posting)