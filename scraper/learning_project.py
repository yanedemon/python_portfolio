#learning project

from urllib.request import urlopen
from bs4 import BeautifulSoup

# lesson 1 - первый взгляд на bs4
# def getTitle(url):
#     try:
#         html = urlopen(url) #инициируем переменную html методом urlopen
#     except HTTPError as e: #предусматриваем исключение HTTPError
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read()) #инициируем bsObject
#         title = bsObj.body.h1 #инициируем заголовок
#     except AttributeError as e: #избегаем исключение
#         return None
#     return title #возвращаем заголовок
# title = getTitle('http://www.pythonscraping.com/pages/page1.html') #извлекаем заголовок с сайта
# if title == None:
#     print('Title could not ve found')
# else:
#     print(title) #печатаем заголовок


# lesson 2 - аргументы .find & .findAll
# html = urlopen('http://pythonscraping.com/pages/warandpeace.html') #получаем ссылку
# bsObj = BeautifulSoup(html)
# nameList = bsObj.findAll('span', {'class': 'green'})
# #nameList = bsObj.findAll(text = 'the prince')
# #print(len(nameList)) #частота вхождений текста the prince
# for name in nameList:
#     print(name.get_text()) #циклом печатаем их

# аргументы .find & .findAll:
# tag .findAll({'h1', 'h2', 'h3'}) - вернуть список всех тегов заголовков
# attributes .findAll('span', {'class': 'green', 'class': 'red'}) - вернуь все теги span задающие зеленый и красный цвет
# recursive True - глубокое исследование потомков элементов; False - исследование тегов верхнего уровня (.findall recursive == True)
# text .findAll(text = 'smthng') - ищет вхождение текста внутри тегов страницы
# limit .find = .findAll(limit == 1) - устанавливает ограничение на поиск значений
# keyword .findAll(id = 'text') - выбор тегов с конкретным атрибутом


# lesson 3 - навигация по дереву на примере интернет-магазина
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bsObj = BeautifulSoup(html)
# print(bsObj.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# дочерние теги всегда на 1 уровень родительского тега, теги-потомки на любой уровень ниже родительского тега
# код выше выводит список строк с названиями продуктов таблицы giftList


# lesson 4 - regexp
# import re
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bsObj = BeautifulSoup(html)
# images = bsObj.findAll('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])

# lesson 5 - lambda
# soup.findAll(lambda tag: len(tag.attrs) == 2) - извлечь все теги, у которых два атрибута


#lesson 6 - краулинг - не подключает к википедии
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bsObj = BeautifulSoup(html)
# for link in bsObj.findALl('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# lesson 7 - куки
# import requests
#
# params = {'username': 'Ryan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
# print('Cooke is set to: ')
# print(r.cookies.get_dict())
# print('------------------')
# print('Going to profile page...')
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies = r.cookies)
# print(r.text)

# lesson 8 - selenium
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# time.sleep(3)
# print(driver.find_element_by_id('content').text)
# driver.close()
