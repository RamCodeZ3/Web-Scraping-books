import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import re
from colorama import init, Fore


URL = 'http://books.toscrape.com/'
answer = requests.get(URL)
x = []
y = []

soup = BeautifulSoup(answer.text, 'html.parser')
books = soup.find_all("article", class_="product_pod")
id_book = 0

for book in books:
    title = book.h3.a["title"]
    price = re.sub(
        r'Â£',
        "",
        book.find("p", class_="price_color").get_text(
            strip=True
            )
        )
    
    x.append(title)
    y.append(float(price))
    id_book += 1
    print('Libro: {:03d}\n Titulo: {} \n Precio:{}\n'.format(id_book, title, price))

plt.bar(x, y, color="skyblue")
plt.title('Gráfico de Barras Simple')
plt.xlabel('Libros')
plt.ylabel('Precios')

# Mostrar el gráfico
plt.show()

