import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    time.sleep(5)
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_1(self, browser):
        browser.get(link)

        login_button = browser.find_element(By.XPATH, '//*[@id="ember33"]')
        login_button.click()

        user_login = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        user_login.send_keys('')

        user_pass = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        user_pass.send_keys('')

        button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
        button.click()
        time.sleep(3)
