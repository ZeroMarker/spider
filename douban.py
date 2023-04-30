import requests
from bs4 import BeautifulSoup

head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

for start in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start}", headers=head)

    print(response.status_code)

    content = response.text
    soup = BeautifulSoup(content, "html.parser")

    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        text = title.string
        if "/" not in text:
            print(text)