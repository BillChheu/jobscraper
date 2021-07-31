import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://news.ycombinator.com/item?id=27699704&p=1")

soup = BeautifulSoup(page.text, "html.parser")

comments = soup.find_all(class_="comment")
#posting = comments[0].find_all(text=re.compile("junior"))


for x in range(len(comments)):
    entryLevelPosting = comments[x].find_all(text=re.compile("junior|^associate|^entry", flags=re.IGNORECASE))
    
    if (entryLevelPosting):
        print(comments[x].get_text('\n'))
    
    
    


#print(posting)