import requests
from bs4 import BeautifulSoup


URL = 'http://books.toscrape.com/'
answer = requests.get(URL)

soup = BeautifulSoup(answer.text, 'html.parser')
titles = soup.find_all("a", title=True)
quantity = 0

for t in titles:
    title_text = t["title"]
    quantity += 1
    print('{}-Libro: {}'.format(quantity, title_text))

print("Hay un total de {}".format(quantity))
