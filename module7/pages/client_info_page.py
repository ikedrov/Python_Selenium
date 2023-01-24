from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from module7.base.base_class import Base


class ClientInfoPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    name = '//input[@id="first-name"]'
    surname = '//input[@id="last-name"]'
    zip_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'


    def get_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_surname(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname)))

    def get_zip_code(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def input_name(self, name):
        self.get_name().send_keys(name)

    def input_surname(self, surname):
        self.get_surname().send_keys(surname)

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)

    def click_continue_button(self):
        self.get_continue_button().click()

    def input_info(self):
        self.get_current_url()
        self.input_name('Ivan')
        self.input_surname('Ivanov')
        self.input_zip_code('123456')
        self.click_continue_button()
