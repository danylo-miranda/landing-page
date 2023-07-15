import requests
from bs4 import BeautifulSoup
import pandas as pd

link = 'https://www.google.com/finance/?hl=pt'

requisicao = requests.get(link)

print(requisicao)
#print(requisicao.text)

site = BeautifulSoup(requisicao.text, 'html.parser')
#print(site.prettify())

titulo = site.find_all('JwB6zf')

print(titulo)

df = pd.DataFrame(columns=['Ação','Nome','Cotação','Pontos','%'])
