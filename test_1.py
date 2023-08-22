import datetime
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys(password_all)
print('Input Password')
button_login = driver.find_element(By.XPATH,"//input[@id='login-button']")
button_login.click()
print('Click Login Button')
# text_products = driver.find_element(By.XPATH,"//span[@class='title']")
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "Products"
# print("GOOD")

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot(name_screenshot)

# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('Good URL')

time.sleep(5)
driver.quit()