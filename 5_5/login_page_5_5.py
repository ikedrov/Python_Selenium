from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def authorization(self, login_name, login_password):
        user_name = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_name)

        password = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(login_password)

        login_button = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        login_button.click()
