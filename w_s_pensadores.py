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

csv_cits = open('cits_pens.csv', 'w') #citações baixadas
csv_writer = csv.writer(csv_cits) #criação do arquivo com as citações
csv_writer.writerow(['pensamento','autor'])

pensamentos = soup.find_all('p', class_='frase fr')

autor = soup.find_all('span', class_='autor')

#loop pra baixar as frases

for pensamento in pensamentos:
    print(f'"{pensamento.text}" - Machads')

    csv_writer.writerow([pensamentos, autor])  # adc os nomes das colunas

"""
FUNCIONA, MAS PRECISA COLOCAR CADA FRASE EM UMA LINHA
ESTÃO TODAS SE REPETINDO NUMA MESMA LINHA (VÁRIAS VEZES)
"""

"""
SERÁ QUE DÁ PRA BAIXAR AS FRASES COMO UMA LISTA?
"""

