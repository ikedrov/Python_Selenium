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
    menu = '//button[@id="react-burger-menu-btn"]'
    about_link = '//a[@id="about_sidebar_link"]'

    def get_select_product1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product1)))

    def get_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_about_link(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_link)))

    def click_select_product1(self):
        self.get_select_product1().click()

    def click_cart(self):
        self.get_cart().click()

    def click_menu(self):
        self.get_menu().click()

    def click_about_link(self):
        self.get_about_link().click()

    def select_product(self):
        self.get_current_url()
        self.click_select_product1()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about_link()
        self.assert_url('https://saucelabs.com/')