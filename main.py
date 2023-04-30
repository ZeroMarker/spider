import requests
from bs4 import BeautifulSoup

head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
response = requests.get("https://books.toscrape.com/", headers=head)
# response = requests.get("https://movie.douban.com/top250", headers=head)

print(response.status_code)


content = response.text
soup = BeautifulSoup(content, "html.parser")

all_prices = soup.findAll("p", attrs={"class": "price_color"})
for price in all_prices:
    print(price.string[2:])

all_titles = soup.findAll("h3")
for title in all_titles:
    link = title.find("a")
    print(link.string)
