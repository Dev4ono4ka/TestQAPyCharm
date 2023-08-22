import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
radio_button.click()

# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
# check_box.click()


# user_name.send_keys(login_standard_user)
# print("Input Login")

time.sleep(3)
driver.quit()#