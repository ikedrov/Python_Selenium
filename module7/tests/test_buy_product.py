#python -m pytest -s -v
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module7.pages.login_page import LoginPage


def test_buy_product():
    browser = webdriver.Chrome()

    login = LoginPage(browser)
    login.authorization()

    shopping_cart_link = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    shopping_cart_link.click()

    success_test = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
    success_test_value = success_test.text
    assert success_test_value == 'YOUR CART'
    time.sleep(5)
    print('Test success')

