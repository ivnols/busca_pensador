'''
SE ESSE LANCE DER CERTO, VOCÊ VAI PODER BUSCAR E BAIXAR TODAS AS CITAÇÕES DE UM DETERMINADO PERSONAGEM
SE VAI CONSEGUIR JUNTAR TUDO NUM CSV
'''
'''
A IDEIA É USAR A FUNÇÃO INPUT PRA MUDAR A URL NA SOURCE, O INPUT VAI SER O NOME DA PESSOA QUE VOCÊ QUISER
'''

from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

url = "https://pensador.com/autor/machado_de_assis/" #adc a url num objeto

font = requests.get(url)

soup = BeautifulSoup(font.content, 'html.parser')

pensamentos = soup.find_all('p', class_='frase fr')

#loop pra baixar as frases

for pensamento in pensamentos:
    print(f'"{pensamento.text}" - Machads')


# print(soup)

# csv_cits = open('cits_pens.csv', 'w') #citações baixadas
#
# csv_writer = csv.writer(csv_cits) #criação do arquivo com as citações
# csv_writer.writerow(['pensador', 'citações','link da citação']) #adc os nomes das colunas
#

#
#     print()
#
#     csv_cits.close()

