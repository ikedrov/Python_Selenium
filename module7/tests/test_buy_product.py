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


def test_buy_product(set_up):
    browser = webdriver.Chrome()

    login = LoginPage(browser)
    login.authorization()

    mp = MainPage(browser)
    mp.select_product()

    cp = CartPage(browser)
    cp.confirm_product()

    cip = ClientInfoPage(browser)
    cip.input_info()

    pp = PaymentPage(browser)
    pp.payment()

    fp = FinishPage(browser)
    fp.finish()

    time.sleep(5)
    browser.quit()

