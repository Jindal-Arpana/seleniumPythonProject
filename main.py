import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open the web Browser
driver = webdriver.Chrome()

# Go to the web page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Locators and actions
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

submit_button_locator = driver.find_element(By.ID, "submit")
submit_button_locator.click()
time.sleep(5)

actual_url = driver.current_url
expected_url = "https://practicetestautomation.com/logged-in-successfully/"
assert actual_url == expected_url

text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
expected_text = "Logged In Successfully"
assert actual_text == expected_text

logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_locator.is_displayed()
