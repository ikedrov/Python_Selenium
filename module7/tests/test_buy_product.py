#python -m pytest -s -v
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module7.pages.cart_page import CartPage
from module7.pages.client_info_page import ClientInfoPage
from module7.pages.login_page import LoginPage
from module7.pages.main_page import MainPage


def test_buy_product():
    browser = webdriver.Chrome()

    print('Start test')

    login = LoginPage(browser)
    login.authorization()

    mp = MainPage(browser)
    mp.select_product()

    cp = CartPage(browser)
    cp.confirm_product()

    cip = ClientInfoPage(browser)
    cip.input_info()

    time.sleep(5)
    print('Test success')

