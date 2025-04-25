import pytest

from pageObject.loggedInSuccessfullyPage import LoggedInSuccessfullyPage
from pageObject.loginPage import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        # Open the web Browser
        login_page.open()

        # Go to the web page
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.get_expected_url == logged_in_page.current_url, "Actual URL isn't the same as expected"
        assert logged_in_page.get_header == "Logged In Successfully", "Expected header is different from" + logged_in_page.get_header
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # driver.maximize_window()
        # time.sleep(5)
        #
        # # Locators and actions
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys("student")
        #
        # password_locator = driver.find_element(By.ID, "password")
        # password_locator.send_keys("Password123")
        #
        # submit_button_locator = driver.find_element(By.ID, "submit")
        # submit_button_locator.click()
        # time.sleep(5)
        #
        # actual_url = driver.current_url
        # expected_url = "https://practicetestautomation.com/logged-in-successfully/"
        # assert actual_url == expected_url
        #
        # text_locator = driver.find_element(By.TAG_NAME, "h1")
        # actual_text = text_locator.text
        # expected_text = "Logged In Successfully"
        # assert actual_text == expected_text
        #
        # logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        # assert logout_button_locator._is_displayed()
