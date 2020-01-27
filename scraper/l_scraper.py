#learning project

from urllib.request import urlopen
from bs4 import BeautifulSoup

# lesson 1
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


# lesson 2
html = urlopen('http://pythonscraping.com/pages/warandpeace.html') #получаем ссылку
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll('span', {'class': 'green'})
#nameList = bsObj.findAll(text = 'the prince')
#print(len(nameList)) #частота вхождений текста the prince
for name in nameList:
    print(name.get_text()) #циклом печатаем их

# аргументы .find & .findAll:
# tag .findAll({'h1', 'h2', 'h3'}) - вернуть список всех тегов заголовков
# attributes .findAll('span', {'class': 'green', 'class': 'red'}) - вернуь все теги span задающие зеленый и красный цвет
# recursive True - глубокое исследование потомков элементов; False - исследование тегов верхнего уровня (.findall recursive == True)
# text .findAll(text = 'smthng') - ищет вхождение текста внутри тегов страницы
# limit .find = .findAll(limit == 1) - устанавливает ограничение на поиск значений
# keyword .findAll(id = 'text') - выбор тегов с конкретным атрибутом
