import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
first_name.send_keys('Ivan')

last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
last_name.send_keys('Terekhov')

mail_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
mail_name.send_keys('Kukareka.ru')


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

input1 = browser.find_element(By.XPATH, '//*[@id="file"]')# добавляем к этому пути имя файла
input1.send_keys(file_path)

submit_name = browser.find_element(By.XPATH, '/html/body/div/form/button')
submit_name.click()

time.sleep(3)
