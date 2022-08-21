# Web_Scraping
Códigos de web scraping desarrollados en python desde diferentes fuentes, para extraer nombre y precio de diferentes productos, para diferentes estructuras de páginas web.

1. BeautifulSoup_notco.py: 
Esta diseñado para hacer web scraping a una pagina web fija, con solo una página de productos.
Se extrae el nombre y precio de cada producto. 
Cabe destacar que en esta página web, el nombre de los productos estan encasillados dentro de una clase: "text-truncate mt-2" que a su vez esta dentro de un "h6".
Es el modelo de web scraping más sencillo puesto que se extrae el nombre y precio mediante sus respectivas clases.

2. BeautifulSoup_pagina_dinamica.py:
Esta diseñado para hacer web scraping a una pagina web dinámica, con varias páginas de productos.
Se extrae la marca y el precio de cada producto, porque el nombre del producto no tiene una clase con la cual se pueda extraer el elemento. 
Cabe destacar que este código esta hecho paso a paso, para comprender el proceso y luego se encuetra en loop final: a partir de la linea 62. 

3. Scrap_Bs4_Selenium.py: 
Esta diseñado para hacer web scraping a una pagina web dinámica, con varias páginas de productos.
Ante la problematica de que en muchas páginas el nombre del producto no contiene una clase se desarrolló este código.
La metodología consiste en filtrar todos los (h1 o h2 o h3 ... donde generalmete se guardan los nombres de los productos) que estan dentro de los item-box.
De esta foorma se extrae el nombre de los productos. 

