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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS()
action = ActionChains(driver)

dobrodel_login = 'it-otdel@solreg.ru'
dobrodel_password = 'soln141500'

def loginInDobrodel():
    driver.get('https://admin.dobrodel.mosreg.ru/')
    driver.find_element_by_name('j_username').send_keys(dobrodel_login)
    driver.find_element_by_name('j_password').send_keys(dobrodel_password)
    driver.find_element_by_id('loginSubmit').click()

def startScraping():
