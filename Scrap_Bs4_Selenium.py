import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import time

# Cambiar las class: hay que poner la clase del precio y la clase de los item-box
# Cambiar el filtro para encontrar el nombre de los productos: h1,h2,h3,h4...

def scrape_page(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()

    df = pd.DataFrame(list(zip([None if x == None else x.string for x in soup.find_all('h1')],
                           [None if x.find(attrs={'class':'product-block-list'}) == None else x.find(attrs={'class':'product-block-list'}).string.replace('£','') for x in soup.find_all(attrs={'class':'col-md-3 col-6 px-2'})])),
                  columns=['product_name','price'])
    
    return df

# Cambiar la pagina web
scrape_page('https://www.emporiovivevegano.cl/productos-veganos?page=1')


# Cambiar el nombre del CSV
def scrape_multiple_pages(url,pages):
    #Input parameters of url and number of pages to scrape. Put {} in place of page number in url.
    page_number = list(range(pages))
    df = pd.DataFrame(columns=['product_name','price'])
    for i in range(len(page_number)): #Loops through each page number in url.
        if requests.get(url.format(i+1)).status_code == 200: #If the url returns an OK 200 reponse, scrape the page. 
            df_page = scrape_page(url.format(i+1))
            df = df.append(df_page)
            time.sleep(1) #Wait 5 seconds.
        else:
            break
    return df.to_csv('emporio_final.csv', index=False)

# Cambiar el paginado de la web y la cantidad de paginas
scrape_multiple_pages('https://www.emporiovivevegano.cl/productos-veganos?page={}',pages=22)