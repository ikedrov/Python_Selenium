#python -m pytest -s -v
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module7.pages.cart_page import CartPage
from module7.pages.client_info_page import ClientInfoPage
from module7.pages.finish_page import FinishPage
from module7.pages.login_page import LoginPage
from module7.pages.main_page import MainPage
from module7.pages.payment_page import PaymentPage


def test_about_link():
    browser = webdriver.Chrome()

    print('Start test')

    login = LoginPage(browser)
    login.authorization()

    mp = MainPage(browser)
    mp.select_menu_about()

    time.sleep(5)
    print('Test success')
    browser.quit()

