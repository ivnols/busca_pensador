"""
SCRIPT DE WEBSCRAPING SEGUINDO O TUTORIAL DE COREY SCHAFER (coreyms.com)
NO TUTORIAL ELE USA O ARGUMEN   TO 'lxml' NO LUGAR DE 'html.parser'...
"""
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com').text #objeto que avisa qual página vc vai pegar as info

soup = BeautifulSoup(source, 'html.parser') #cria o objeto com as informações do html (código fonte)

print(soup)

csv_file = open('cms_scrape.csv', 'w') #esse w é pra 'write csv'

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text  # quando adiciona .text o cara tem os dados em formato de plain text
    print(headline)  # mostra a seção do html que tem a info    desse objeto

    summary = article.find('div',class_='entry-content').p.text  # aqui vc cria um objeto pra ver o resumo (em texto) do artigo no site do cara
    print(summary)

    '''ESSA FUNÇÃO TRY SERVE PRA """DRIBLAR""" ALGUM LINK QUE NÃO TENHA UM DOS ARGUMENTOS
    NESSE CASO, ALGUNS ARQUIVOS N VÃO TER LINK DE VÍDEO
    AÍ ELE SUBSTITUI POR NONE QUANDO FOR PRINTAR A PARADA
    '''

    # NA VDD A GNT NÃO VAI PRECISAR DESSA PARTE, POR ENQUANTO
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
                yt_link = None

    print(yt_link )

    print()

    csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()
#
# # comando pra pegar informação de link do vídeo que tem no artigo
#
# # transforma o link do vídeo numa lista. cada elemento do link vira um elemento da lista
# # pega uma determinada informação do link
#
#       # isso é o link real pro vídeo
#
#
# #try funciona como um tipo de exceção
#
#
# #print(article.prettify()) #.prettify mostra as info do html com a mesma formatação
#
