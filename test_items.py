import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checking_store_button(browser):
    browser.get(link)
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

    