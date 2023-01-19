from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page_5_5 import LoginPage

class MainPage(LoginPage):

    def check_main_page(self):
        check_products = self.browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        check_products_value = check_products.text
        assert check_products_value == 'PRODUCTS'
        print('Check Products ok')

    def logout(self):
        burger_menu = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu_button_container"]/div/div[1]/div')))
        burger_menu.click()
        logout_button = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
        logout_button.click()



