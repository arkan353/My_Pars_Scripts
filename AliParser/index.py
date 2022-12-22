import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
tParam = []
tParam2 = []

for i in range(1, 15):
    url = "https://aliexpress.ru/wholesale?SearchText=%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+poco+m5s&g=y&page=" + str(i)
    print(url)
    r = requests.get(url)
    r.text
    soup = BeautifulSoup(r.text, 'lxml')
    #Парсинг цены
    #snow-price_SnowPrice__mainM__18x8np
    priceText = soup.find_all("div", class_="snow-price_SnowPrice__mainM__18x8np")
    nameText = soup.find_all('div', class_="product-snippet_ProductSnippet__name__lido9p")
   

    for name in nameText:
        tParam.append(name.text)

    for param in priceText:
        tParam2.append(param.text)
    
    
    print(tParam, tParam2)
    table = pd.DataFrame({
    'Name':tParam,    
    'Price':tParam2
    })
    
table.to_excel('./teams.xlsx')