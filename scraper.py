import requests
from bs4 import BeautifulSoup
import csv

#Url alvo
url = 'https://books.toscrape.com/'

resposta = requests.get(url)
resposta.encoding = 'UTF-8'

soup = BeautifulSoup(resposta.text, 'html.parser')

livros = soup.find_all('article', class_='product_pod')

# for livro in livros:
#     titulo = livro.h3.a['title']
#     link = livro.h3.a['href']
#     preco = livro.find('p', class_='price_color').text
#     print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     print(titulo)
#     print(url + link)
#     print(preco)

with open('relatorio.csv', 'w', newline="",encoding='UTF-8') as csv_file:
    escritor = csv.writer(csv_file)

    escritor.writerow([titulo, preco, link])

    for livro in livros:
        titulo = livro.h3.a['title']
        link = livro.h3.a['href']
        preco = livro.find('p', class_='price_color').text
        escritor.writerow([titulo, preco, url+link])
