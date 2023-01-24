from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from module7.base.base_class import Base


class CartPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    checkout_button = '//button[@id="checkout"]'

    def get_checkout_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def click_checkout_button(self):
        self.get_checkout_button().click()


    def confirm_product(self):
        self.get_current_url()
        self.click_checkout_button()
