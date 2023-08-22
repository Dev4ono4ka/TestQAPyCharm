import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"
total = ''

def answer():
!!!

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_1(self, browser):
        browser.get(link)

        login_button = browser.find_element(By.XPATH, '//*[@id="ember60"]')
        login_button.send_keys()

        user_login = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        user_login.send_keys('логин')

        user_pass = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        user_pass.send_keys('пароль')

        button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
        button.click()

        textareal = browser.find_element(By.XPATH,'//*[@id="ember106"]')
        textareal.send_keys('answer')

        p1 = browser.find_element(By.XPATH,'//*[@id="ember102"]/p')
        p1 = p1.text

        if p1 != 'Correct'
            total += p1


        time.sleep(3)