import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

fechas = []
pibs = []
vars = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

fecha_list=list()
pib_eur_list=list()
pib_dol_list=list()
variacion_list=list()

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')
tabla = soup.find('table', attrs={'class':'table tabledat table-striped table-condensed table-hover'})

filas = tabla.find_all('tr')

for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        fecha = celdas[0].string
        #pib_eur = float(re.sub(r'\D', '', celdas[1].string))
        pib_eur = celdas[1].string
        pib_dol = float(re.sub(r'\D', '', celdas[2].string))
        #print(pib_dol)
        variacion = celdas[3].string
        fecha_list.append(fecha)
        pib_eur_list.append(pib_eur)
        pib_dol_list.append(pib_dol)
        variacion_list.append(variacion)


df = pd.DataFrame({'Año':fecha_list,'PIB (EUROS)':pib_eur_list, 'PIB (DOLARES)':pib_dol_list, 'Variacion': variacion_list})
df.to_csv('pib_ec.csv', index=False, encoding='utf-8')


