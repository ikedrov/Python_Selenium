import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page_5_5 import LoginPage
from main_page import MainPage

class UserLogin:

    def login_logout(self):
        browser = webdriver.Chrome()
        main_url = 'https://saucedemo.com/'
        browser.get(main_url)

        list_of_users = ('standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user')
        password_all = 'secret_sauce'

        login = LoginPage(browser)
        for i in list_of_users:
            login.authorization(i, password_all)
            time.sleep(6)
            if i == 'locked_out_user':
                user_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
                user_name.send_keys(Keys.BACKSPACE * 15)
                password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
                password.send_keys(Keys.BACKSPACE * 12)
                continue

            check = MainPage(browser)
            check.check_main_page()

            logout = MainPage(browser)
            logout.logout()

            print('Test is finished!')


test = UserLogin()
test.login_logout()



