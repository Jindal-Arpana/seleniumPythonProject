import pytest
from pageObject.loginPage import LoginPage

""" using parametrized decorator here, 
to not hard code the values and 
ease of automation framework """


class TestNegativeScenarios:

    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_msg",
                             [("incorrectuser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectpassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_msg):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_msg() == expected_error_msg, "This error message is not expected"


"""
   
   ''' This function was used before PoM was created ''' 
   
        # Go to the web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(5)

        # Locators and actions
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        time.sleep(2)

        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)
        time.sleep(2)

        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(5)

        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator._is_displayed(), "Error message isn't displayed"

        error_msg = error_msg_locator.text
        # expected_error_msg = "Your username is invalid!"
        assert error_msg == expected_error_msg, "Error message isn't expected"

    def test_negative_username(self, driver):
        # Go to the web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(5)

        # Locators and actions
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectuser")
        time.sleep(2)

        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")
        time.sleep(2)

        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(5)

        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator._is_displayed(), "Error message isn't displayed"

        error_msg = error_msg_locator.text
        expected_error_msg = "Your username is invalid!"
        assert error_msg == expected_error_msg, "Error message isn't expected"

    def test_negative_password(self, driver):
        # Go to the web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(5)

        # Locators and actions
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        time.sleep(2)

        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password12345")
        time.sleep(2)

        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(5)

        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator._is_displayed(), "Error message isn't displayed"

        error_msg = error_msg_locator.text
        expected_error_msg = "Your password is invalid!"
        assert error_msg == expected_error_msg, "Error message isn't expected"

"""