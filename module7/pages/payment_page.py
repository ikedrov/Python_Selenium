from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from module7.base.base_class import Base


class PaymentPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_button = '//button[@id="finish"]'

    def get_finish_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def click_finish_button(self):
        self.get_finish_button().click()

    def payment(self):
        self.get_current_url()
        self.click_finish_button()
