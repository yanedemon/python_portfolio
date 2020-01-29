# session = requests.Session()
# session.post('https://admin.dobrodel.mosreg.ru/CardEditListExt?show=/Topic?id=3616609', {'email': 'it-otdel@solreg.ru', 'password': 'soln141500'})
# html = urlopen('https://admin.dobrodel.mosreg.ru/CardEditListExt?show=/Topic?id=3616609')
# bsObj = BeautifulSoup(html.read())
# title = bsObj.findAll('div')
# print(title)
#
# Пока не работает, но скоро решим
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

params = {'j_username': 'it-otdel@solreg.ru', 'j_password': 'soln141500'}
r = requests.post('http://admin.dobrodel.mosreg.ru/login', params)
print('Cookie is set to: ')
print(r.cookies.get_dict())
print('------------------')
print('Going to profile page...')
r = requests.get('http://admin.dobrodel.mosreg.ru/CardEditListExt', cookies = r.cookies)
print(r.text)
