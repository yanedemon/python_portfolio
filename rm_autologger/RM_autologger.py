from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_today.clicked.connect(self.select_today)

    def select_today(self):
        openBrowser()
        loginInRM()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


driver = webdriver.Chrome()
action = ActionChains(driver)

now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year

login_rm = '###'
password_rm = '###'

def dataVerify():
    global day
    if day == 1:
        if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
            day = 31
            month = month - 1
        elif month == 3:
            day = 29
            month = 2
        else:
            day = 30
            month = month - 1
    else:
           day -= 1

def changeDate():
    date_element = driver.find_element_by_id('eq-values-is_garbage_not_taken_out_date_full_1')
    if day < 10:
        date_element.send_keys(str(year) + '-' + str(month) + '-' + '0' + str(day))
    elif month < 10:
        date_element.send_keys(str(year) + '-' + '0' + str(month) + '-' + str(day))
    elif day < 10 and month < 10:
        date_element.send_keys(str(year) + '-' + '0' + str(month) + '-' + '0' + str(day))
    else:
        date_element.send_keys(str(year) + '-' + str(month) + '-' + str(day)) #приписываем 0 в дате, если день/месяц меньше 10

def inputDate():
    global day
    print('Введите дату или выберите требуемую из списка: T - сегодня, Y - вчера, L - позавчера, D - ввести дату самостоятельно', end = '\n > ')
    input_date = str(input())
    if input_date == 't' or input_date == 'T':
        print('Выбрана дата: ' + str(year) + '-' + str(month) + '-' + str(day))
        changeDate()
    elif input_date == 'y' or input_date == 'Y':
        dataVerify()
        print('Выбрана дата: ' + str(year) + '-' + str(month) + '-' + str(day))
        changeDate()
    elif input_date == 'l' or input_date == 'L':
        dataVerify()
        day -= 1
        print('Выбрана дата: ' + str(year) + '-' + str(month) + '-' + str(day))
        changeDate()
    elif input_date == 'd' or input_date == 'D':
        print('Введите дату в формате YYYY-MM-DD: ')
        input_date = str(input())
        driver.find_element_by_id('eq-values-is_garbage_not_taken_out_date_full_1').send_keys(input_date)
    else:
        print('Неправильное значение.')
        inputDate()

def openBrowser():
    driver.get('https://mep-check.rm.mosreg.ru/')

def loginInRM():
    driver.find_element_by_name('username').send_keys(login_rm)
    driver.find_element_by_name('password').send_keys(password_rm)
    driver.find_element_by_name('login').click()

def startWorking():
    driver.find_element_by_link_text('Все мои контейнерные площадки').click()
    driver.find_element_by_id('f-fields-list').click()
    driver.find_element_by_id('eq-value--is_garbage_not_taken_out_date_full').click()
    driver.find_element_by_link_text('Сохранить').click()
    time.sleep(1)
    driver.find_elements_by_class_name('eq-field-title')[1].click()
    driver.find_element_by_id('eq-values-is_garbage_not_taken_out_date_full_1')
    inputDate() #предлагаем ввести дату
    time.sleep(1)
    driver.find_element_by_class_name('eq-save').click()
    driver.find_element_by_id('eq-apply-query').click()
    time.sleep(1)
    driver.find_element_by_id('check_all').click()
    time.sleep(1)
    action.context_click(driver.find_element_by_class_name('hascontextmenu')).perform()
    time.sleep(1)
    driver.find_element_by_class_name('icon-copy').click()
    time.sleep(1)
    driver.find_element_by_id('issue_project_id').click()
    driver.find_element_by_id('issue_project_id').send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id('issue_project_id').send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element_by_id('issue_tracker_id').click()
    driver.find_element_by_id('issue_tracker_id').send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_id('issue_tracker_id').send_keys(Keys.RETURN)
    driver.find_element_by_name('commit').click()

#main()
openBrowser()
loginInRM()
startWorking()

### TODO:
### Запилить гуи
### Также нужно принимать логин и пароль от пользователя в гуи
### И хранить его отдельной переменной, чтобы не вводить каждый раз
### ????
### PROFIT!!
