'''
1.открыть календарь на сайте demoqa.com

2.с помощью библиотеки datetime установить дату на 10 дней позже (ПОЗЖЕ - значит + 10 дней) чем существующая, не контактирую с локатором нынешней даты (т.е. не используя переменную locator как на уроке) и ввести ее в поле даты
'''

import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
main_url = 'https://demoqa.com/date-picker'
browser.get(main_url)

calendar = browser.find_element(By.XPATH, '//input[@id = "datePickerMonthYearInput"]')
time.sleep(3)

now_date = datetime.date.today()
#print(now_date)
new_date = str(now_date + datetime.timedelta(days=10)).split('-')
new_date_formated = f'{new_date[1]}/{new_date[2]}/{new_date[0]}'
#print(new_date_formated)

calendar.send_keys(Keys.BACKSPACE * 10)
calendar.send_keys(new_date_formated)
calendar.send_keys(Keys.RETURN)
time.sleep(5)

