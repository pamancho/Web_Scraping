# https://www.youtube.com/watch?v=y0TpyWhrcDk
# https://www.youtube.com/watch?v=gzLIJZkOGYQ

from urllib import response
import pandas as pd
import requests
from bs4 import BeautifulSoup

# #stablece la pagina web 
website = 'https://www.emporiovivevegano.cl/productos-veganos'

response = requests.get(website)

print(response.status_code)

# Se crea la sopa que recorre la pagina web
soup = BeautifulSoup(response.content, 'html.parser')

# Se obtienen todos los item-box de la pagina 1
results = soup.find_all('div', {'class': 'col-md-3 col-6 px-2'}) 
print(len(results))

# Se extrae la marca y precio del primer item-box
# Sacando marca
print(results[0].find('span', {'class': 'brand'}).get_text())
# Scando precio
print(results[0].find('span', {'class': 'product-block-list'}).get_text())

# Se genera un loop para extraer el precio y marca de todos los item-box de la pagina 1
# loop para una pagina
product_name = []
product_price = []

for result in results:

    # Marca 
    try:
        product_name.append(result.find('span', {'class': 'brand'}).get_text())
    except:
        product_name.append('n/a')

    # Precio
    try:
        product_price.append(result.find('span', {'class': 'product-block-list'}).get_text())
    except:
        product_price.append('n/a')


# Se printe para ver que todo este bien
print(product_price)
print(len(product_price))
print(len(product_name))

# Se genera un df con los productos de la pagina 1
pg_uno_emporio = pd.DataFrame({'Marca': product_name, 'Price': product_price})
print('================ DataFrame =================')
print(pg_uno_emporio)
# Para guardar este df a dataframe
# pg_uno_emporio.to_csv('emporio_pag_1.csv', index=False)


# Loop para todas las paginas dentro de la pagina web
product_name = []
product_price = []

# son 22 paginas (el 23 se excluye en el range)
for i in range(1, 23):

    # website
    website = 'https://www.emporiovivevegano.cl/productos-veganos?page=' + str(i)

    # request
    response = requests.get(website)

    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')

    # results
    results = soup.find_all('div', {'class': 'col-md-3 col-6 px-2'}) 

    # loop trough results
    for result in results:
        # Marca 
        try:
            product_name.append(result.find('span', {'class': 'brand'}).get_text())
        except:
            product_name.append('n/a')

        # Precio
        try:
            product_price.append(result.find('span', {'class': 'product-block-list'}).get_text())
        except:
            product_price.append('n/a')

df_emporio = pd.DataFrame({'Marca': product_name, 'Price': product_price})
df_emporio.to_csv('emporio.csv', index=False)