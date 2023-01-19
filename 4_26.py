from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('Приветствую тебя в нашем интернет магазине!')
print('Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, '
      '3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, '
      '6 - Test.allTheThings() T-Shirt (Red)')

product = input()

all_products_names = {'1': '//a[@id="item_4_title_link"]', '2': '//a[@id="item_0_title_link"]',
                      '3': '//a[@id="item_1_title_link"]', '4': '//a[@id="item_5_title_link"]',
                      '5': '//a[@id="item_2_title_link"]', '6': '//a[@id="item_3_title_link"]'}
all_products_prices = {'1': '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div', '2': '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div',
                       '3': '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div', '4': '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div',
                       '5': '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div', '6': '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div'}
all_products_links = {'1': '//button[@id="add-to-cart-sauce-labs-backpack"]', '2': '//button[@id="add-to-cart-sauce-labs-bike-light"]',
                      '3': '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]', '4': '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]',
                      '5': '//button[@id="add-to-cart-sauce-labs-onesie"]', '6': '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'}

def user_product(product):
    browser = webdriver.Chrome()
    main_url = 'https://saucedemo.com/'
    browser.get(main_url)

    login_standard_user = 'standard_user'
    password_all = 'secret_sauce'

    user_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
    user_name.send_keys(login_standard_user)
    password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
    password.send_keys(password_all)
    login_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
    login_button.click()

    product1 = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, all_products_names[product])))
    product1_value = product1.text
    product1_price = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, all_products_prices[product])))
    product1_value_price = product1_price.text
    select_product = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, all_products_links[product])))
    select_product.click()

    shopping_cart_link = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    shopping_cart_link.click()

    product1_cart = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="inventory_item_name"]')))
    product1_cart_value = product1_cart.text
    product1_cart_price = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="inventory_item_price"]')))
    product1_cart_price_value = product1_cart_price.text
    assert product1_cart_value == product1_value
    print(f'Product {product} value ok')
    assert product1_cart_price_value == product1_value_price
    print(f'Product {product} price ok')

    checkout_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="checkout"]')))
    checkout_button.click()

    input_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="first-name"]')))
    input_name.send_keys('Ivan')
    input_last_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="last-name"]')))
    input_last_name.send_keys('Ivanov')
    input_zip = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="postal-code"]')))
    input_zip.send_keys('12345')
    continue_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="continue"]')))
    continue_button.click()

    product1_final = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="inventory_item_name"]')))
    product1_final_value = product1_final.text
    product1_final_price = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="inventory_item_price"]')))
    product1_final_price_value = product1_final_price.text
    assert product1_final_value == product1_cart_value
    print(f'Product {product} final value ok')
    assert product1_final_price_value == product1_cart_price_value
    print(f'Product {product} final price ok')

    action = ActionChains(browser)
    finish_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="finish"]')))
    action.move_to_element(finish_button)
    finish_button.click()
    browser.quit()

if product in ('1', '2', '3', '4', '5', '6'):
    user_product(product)
else:
    print('Число должно быть от одного до 6')

