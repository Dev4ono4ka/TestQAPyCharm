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

menu = driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']")
menu.click()
print('Click Menu Button')
time.sleep(3)
link_about = driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']")
link_about.click()
print("Click Link Button")

driver.back()
print("Go Back")
time.sleep(3)
driver.forward()
print("Go Forward")