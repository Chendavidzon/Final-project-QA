import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
our_url = 'https://www.saucedemo.com/'


def login(driver, username, password):
    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    user_name.send_keys(username)
    time.sleep(1)
    pass_word = driver.find_element(By.CSS_SELECTOR, '#password')
    pass_word.send_keys(password)
    time.sleep(1)
    signup = driver.find_element(By.CSS_SELECTOR, '#login-button')
    signup.click()
    time.sleep(3)

def add_chart(driver, product, added):
    backpack = driver.find_element(By.CSS_SELECTOR, product)
    backpack.click()
    time.sleep(2)
    add_to_chart = driver.find_element(By.CSS_SELECTOR, added)
    add_to_chart.click()
    time.sleep(2)

def my_cart(driver):
    cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    cart.click()
    time.sleep(2)
    checkout_selector = driver.find_element(By.CSS_SELECTOR, '#checkout')
    checkout_selector.click()
    time.sleep(2)

def checkout_info(driver, firstname, lastname, zipcode):
    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys(firstname)
    time.sleep(1)
    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.send_keys(lastname)
    time.sleep(1)
    zip_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    zip_code.send_keys(zipcode)
    time.sleep(1)
    continue_button = driver.find_element(By.CSS_SELECTOR, '#continue')
    continue_button.click()
    finish_button = driver.find_element(By.CSS_SELECTOR, '#finish')
    finish_button.click()
    time.sleep(2)

def price_sort(driver):
    sort_by = driver.find_element(By.CSS_SELECTOR, '#header_container > div.header_secondary_container > div > span > select')
    sort_by.click()
    time.sleep(2)
    low_to_high = driver.find_element(By.CSS_SELECTOR, '#header_container > div.header_secondary_container > div > span > select > option:nth-child(3)')
    low_to_high.click()
    time.sleep(2)
