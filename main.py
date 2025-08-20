import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
import os
import csv


URL = 'http://books.toscrape.com/'
answer = requests.get(URL)
x = []
y = []

os.makedirs("output_data", exist_ok=True)

with open('output_data/book.csv', 'w', newline='', encoding='utf-8') as file:
    write = csv.writer(file)
    write.writerow(['ID', 'Titulo', 'Precio(£)', 'Precio($)', 'Stock'])

soup = BeautifulSoup(answer.text, 'html.parser')
books = soup.find_all("article", class_="product_pod")


def print_data():
    try:
        id_book = 1
        with open(
                "output_data/book.csv",
                "a",
                newline="",
                encoding="utf-8") as file:
            write = csv.writer(file)
            for book in books:
                title = book.h3.a["title"]
                price = re.sub(
                        r'Â£',
                        "",
                        book.find("p", class_="price_color").get_text(
                            strip=True
                        )
                )

                stock = re.sub(
                    r'<i class="icon-star"></i>',
                    "",
                    book.find("p", class_='instock availability').get_text(
                        strip=True
                    )
                )

                print(
                    f"Libro: {id_book:03d}\n"
                    f" Titulo:\n  {title}\n"
                    f" Precios:\n  £{price} - ${float(price) * 1.35:.2f}\n"
                    f" Stock:\n  {stock}\n"
                    "_____________________________________________________"
                )

                x.append("ID:{:03d}".format(id_book))
                y.append(float(price))

                write.writerow([
                    id_book,
                    title,
                    price,
                    round(float(price) * 1.35, 2),
                    stock
                ])

                id_book += 1

        plt.barh(x, y, color="skyblue")
        plt.title("Precios de libros")
        plt.xlabel("Precio (£)")
        plt.ylabel("ID del libro")
        plt.tight_layout()

        # Mostrar el gráfico
        plt.savefig("output_data/grafico.png", dpi=200, bbox_inches="tight")

    except Exception as e:
        print("Hubo un error en la ejecurcion de la funcion: ", e)


if __name__ == '__main__':
    print_data()
