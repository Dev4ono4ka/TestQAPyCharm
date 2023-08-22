import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

want = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
want.click()

alert = browser.switch_to.alert
alert.accept()

span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

confirm = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
confirm.click()

time.sleep(3)