
# 📚 Web Scraping de Books to Scrape con Python  

Este proyecto realiza **web scraping** en la página [Books to Scrape](http://books.toscrape.com/) para extraer información sobre los libros disponibles (título y precio).  
Con los datos obtenidos, se genera un **gráfico de barras horizontal** que muestra el precio de cada libro en libras (£). Además, se calcula y muestra el equivalente en dólares (USD).  

---

## 🚀 Tecnologías utilizadas  
- [Python 3](https://www.python.org/)  
- [Requests](https://docs.python-requests.org/en/master/) → Para realizar la petición HTTP.  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) → Para parsear y extraer datos del HTML.  
- [Matplotlib](https://matplotlib.org/stable/) → Para graficar los precios de los libros.  
- [Regex (re)](https://docs.python.org/3/library/re.html) → Para limpiar los datos de los precios.  

---

## 📂 Estructura del proyecto  
📦 proyecto-scraping <br/>
┣ 📂 output_data <br/>
┃ ┗ 📜 grafico.png # Gráfico generado con los precios <br/>
┣ 📜 main.py # Código principal <br/>
┣ 📜 README.md # Documentación del proyecto

---
## ⚙️ Instalación y uso  

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/tuusuario/proyecto-scraping.git
   cd proyecto-scraping
