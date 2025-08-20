import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re


URL = 'http://books.toscrape.com/'
answer = requests.get(URL)
x = []
y = []

soup = BeautifulSoup(answer.text, 'html.parser')
books = soup.find_all("article", class_="product_pod")


def print_data():
    try:
        id_book = 1
        for book in books:
            title = book.h3.a["title"]
            price = re.sub(
                    r'Â£',
                    "",
                    book.find("p", class_="price_color").get_text(
                        strip=True
                    )
            )

            x.append("ID:{:03d}".format(id_book))
            y.append(float(price))
            print('Libro: {:03d}\n Titulo: {} \n Precio:{}\n'.format(
                id_book,
                title,
                price
                ))
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
