import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(3)
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('standard_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()

    @pytest.mark.xfail
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('locked_out_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()