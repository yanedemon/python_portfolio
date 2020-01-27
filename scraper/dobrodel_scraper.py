from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

session = requests.Session()
session.post('https://admin.dobrodel.mosreg.ru/', {'email': 'it-otdel@solreg.ru', 'password': 'soln141500'})
html = urlopen('https://admin.dobrodel.mosreg.ru/CardEditListExt?show=/Topic?id=3616609')
bsObj = BeautifulSoup(html.read())
title = bsObj.findAll('div')
print(title)

# Пока не работает, но скоро решим
