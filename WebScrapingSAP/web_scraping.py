
import pandas as pd
import requests

from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'

html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.content, 'html.parser')

titulo_datos = soup.h1.string

tabla = soup.find('table')

filas = tabla.find_all('tr')


nombres = []
apellidos = []


for fila in filas:

    celdas = fila.find_all('td')
    if len(celdas)>0:

        nombres.append(celdas[1].string)
        apellidos.append(celdas[2].string)


        print(nombres)
        print(apellidos)


df = pd.DataFrame({'Nombre':nombres,'Apellido':apellidos})
df.to_csv('clientes.csv', index=False, encoding='utf-8')

