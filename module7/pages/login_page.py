from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from module7.base.base_class import Base


class LoginPage(Base):

    url = 'https://saucedemo.com/'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'

    def get_user_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def authorization(self):
        self.browser.get(self.url)
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()
