'''
1.Авторизоваться на сайте

2.Выбрать 2 товара

3.Сохранить в переменные названия и цены товаров

4.Пройти весь БП, на моменте оплаты товара сверить сохраненные значения, а так же что система правильно посчитала сумму товаров (отдельно считаем сумм товаров и проверяем с тем что говорит нам система)
'''


import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
main_url = 'https://saucedemo.com/'
browser.get(main_url)

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
login_button = browser.find_element(By.XPATH, '//input[@id="login-button"]')
login_button.click()
time.sleep(3)

product1 = browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
product1_value = product1.text
product1_price = browser.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
product1_price_value = product1_price.text

product2 = browser.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
product2_value = product2.text
product2_price = browser.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
product2_price_value = product2_price.text

select_product1 = browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product1.click()
select_product2 = browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
select_product2.click()

shopping_cart_link = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
shopping_cart_link.click()
time.sleep(3)

product1_cart = browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
product1_cart_value = product1_cart.text
product1_cart_price = browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
product1_cart_price_value = product1_cart_price.text
assert product1_cart_value == product1_value
print('Product 1 value ok')
assert product1_cart_price_value == product1_price_value
print('Product 1 price ok')

product2_cart = browser.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
product2_cart_value = product2_cart.text
product2_cart_price = browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
product2_cart_price_value = product2_cart_price.text
assert product2_cart_value == product2_value
print('Product 2 value ok')
assert product2_cart_price_value == product2_price_value
print('Product 2 price ok')

checkout_button = browser.find_element(By.XPATH, '//button[@id="checkout"]')
checkout_button.click()
time.sleep(3)

input_name = browser.find_element(By.XPATH, '//input[@id="first-name"]')
input_name.send_keys('Ivan')
input_last_name = browser.find_element(By.XPATH, '//input[@id="last-name"]')
input_last_name.send_keys('Ivanov')
input_zip = browser.find_element(By.XPATH, '//input[@id="postal-code"]')
input_zip.send_keys('12345')
continue_button = browser.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()
time.sleep(3)

product1_final = browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
product1_final_value = product1_final.text
product1_final_price = browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
product1_final_price_value = product1_final_price.text
assert product1_final_value == product1_cart_value
print('Product 1 final value ok')
assert product1_final_price_value == product1_cart_price_value
print('Product 1 final price ok')

product2_final = browser.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
product2_final_value = product2_final.text
product2_final_price = browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
product2_final_price_value = product2_final_price.text
assert product2_final_value == product2_cart_value
print('Product 2 final value ok')
assert product2_final_price_value == product2_cart_price_value
print('Product 2 final price ok')

action = ActionChains(browser)
finish_button = browser.find_element(By.XPATH, '//button[@id="finish"]')
action.move_to_element(finish_button)

final_price = browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
final_price_value = final_price.text.split('$')
cart_summ = float(product1_final_price_value[1:]) + float(product2_final_price_value[1:])
final_summ = float(final_price_value[1])
assert final_summ == cart_summ
print('Summ ok')

finish_button.click()
time.sleep(3)
print('All ok')

browser.quit()
