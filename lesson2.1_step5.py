from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.XPATH,"//span[@id='input_value']")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)

input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
input2.click()

input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
input3.click()

button1 = browser.find_element(By.XPATH,"//button[@class='btn btn-default']")
button1.click()

time.sleep(3)
browser.quit()