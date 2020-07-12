#docker отказался устанавливаться на мою сборку windows, behave тоже породил тьму ошибок во время установки
#поэтому всё реализовано циклом на селене и time для пауз

from selenium import webdriver
import time

driver = webdriver.Chrome()

def startWorking(): #Проходим первый раз
    driver.get('http://qa-assignment.oblakogroup.ru/board/:dmitry_zverev')
    element = list(driver.find_elements_by_class_name('icheckbox_square-blue'))
    index = 0
    for elements in element:
        try: #Я использовал перехват исключений, чтобы дойти до конца списка и перейти к следующей функции
            index += 1
            time.sleep(0.5)
            element[index].click()
        except:
            IndexError
            print('First part completed')

def continueWorking(): #Проходим второй раз
    element = list(driver.find_elements_by_class_name('icheckbox_square-blue'))
    index = 0
    for elements in element:
        try:
            index += 1
            time.sleep(0.5)
            element[index].click()
        except:
            IndexError
            print('All test completed')

startWorking()
continueWorking()