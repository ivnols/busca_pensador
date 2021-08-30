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

source = requests.get('https://www.pensador.com/autor/clarice_lispector/').text
soup = BeautifulSoup(source, 'html.parser')
csv_cits = open('cits_pens.csv', 'w') #citações baixadas

csv_writer = csv.writer(csv_cits) #criação do arquivo com as citações
csv_writer.writerow(['pensador', 'citações','link da citação']) #adc os nomes das colunas

for pensamento in soup.find_all('thought-card'):
    frase = pensamento.p.text

    print()

    csv_cits.close()

