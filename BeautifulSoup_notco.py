from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.fullcongelados.cl/collection/otros-productos-veganos?limit=24&with_stock=0&order=name&way=ASC'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# =================== Precios =======================

precio = soup.find_all('div', class_='bs-product-final-price')
print(precio)

precios = list()

for i in precio:
    precios.append(i.text)

print(precios)


# =================== Nombre del producto ========================

nombre = soup.find_all('h6', class_='text-truncate mt-2')

nombres = list()

for i in nombre:
    nombres.append(i.text)

print(nombres)


# =================== Se guarda en un csv =================

congelados = pd.DataFrame({'Nombre': nombres, 'Precios': precios})
print(congelados)

congelados.to_csv('congelados.csv', index=False)