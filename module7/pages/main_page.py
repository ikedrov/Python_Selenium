from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from module7.base.base_class import Base


class MainPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    select_product1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//a[@class="shopping_cart_link"]'

    def get_select_product1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product1)))

    def get_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def click_select_product1(self):
        self.get_select_product1().click()

    def click_cart(self):
        self.get_cart().click()

    def select_product(self):
        self.get_current_url()
        self.click_select_product1()
        self.click_cart()
