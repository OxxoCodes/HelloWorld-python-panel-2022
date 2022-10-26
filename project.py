import requests
from bs4 import BeautifulSoup

targetURL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

result = requests.get(targetURL)
html = result.content
soup = BeautifulSoup(html, features="html.parser")

for toRemove in soup(["script", "style"]):
    toRemove.extract()

allText = soup.get_text()

with open("archive.txt", "w") as f:
    f.write(allText)