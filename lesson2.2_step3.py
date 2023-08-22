import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text
num_1 = int(num_1)
num_2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text
num_2 = int(num_2)
value = str(num_1 + num_2)
print(value)



select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(value)

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()

time.sleep(10)
browser.quit()