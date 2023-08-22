import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element(By.ID,"user-name" ) #ID
# user_name = driver.find_element(By.NAME,"user-name" ) #NAME
# user_name = driver.find_element(By.XPATH,"//*[@id='user-name']" ) #XPATH
#user_name = driver.find_element(By.XPATH,"//input[@id='user-name']") # IDXPATH
user_name = driver.find_element(By.XPATH,"//input[@data-test='username']") #data-test xpath
user_name.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR,"#password") #CSS_SELECTOR xpath
password.send_keys('secret_sauce')

button_login = driver.find_element(By.XPATH,"//input[@value='Login']")
button_login.click()




time.sleep(10)
driver.quit()