import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.exceptionsPage import ExceptionsPage


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row2 input should be displayed, but it's not"

    # """
    #
    # ''' This function was used before PoM was created '''
    #         # Open the URL
    #         driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    #
    #         # Click on add button
    #         add_btn_locator = driver.find_element(By.ID, "add_btn")
    #         add_btn_locator.click()
    #
    #         wait = WebDriverWait(driver, 10)
    #         row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
    #
    #         # Verify row2 is added
    #         assert row2_input_element.is_displayed(), "Row2 input should be displayed but, it's not"
    # """

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row2 input should be displayed but its not"
        exceptions_page.add_second_food("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not expected"

    """
    # Open the URL
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    # Click on add button
    add_btn_locator = driver.find_element(By.ID, "add_btn")
    add_btn_locator.click()

    wait = WebDriverWait(driver, 10)
    row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

    # Verify row2 is added
    assert row2_input_element.is_displayed(), "Row2 input should be displayed but its not"
    row2_input_element.send_keys("Pasta")

    # Push save button
    save_button_element = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
    save_button_element.click()

    # Verify text saved
    confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
    confirmation_msg = confirmation_element.text
    assert confirmation_msg == "Row 2 was saved", "Confirmation message is not expected"
    
    """

    @pytest.mark.exceptions
    @pytest.mark.invalid_element
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row_1_input("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Confirmation message is not expected"

    """
    
    # Open the URL
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    # Clear input field
    row1_edit_button_element = driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Edit']")
    row1_edit_button_element.click()
    pizza_element = driver.find_element(By.XPATH, "//input[@type='text' and @value='Pizza']")
    pizza_element.clear()

    # Type text into the input field

    pizza_element.send_keys("Sushi")
    row1_save_button_element = driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']")
    row1_save_button_element.click()

    # Verify text changed and saved
    wait = WebDriverWait(driver, 10)
    confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
    confirmation_msg = confirmation_element.text
    assert confirmation_msg == "Row 1 was saved", "Confirmation message is not expected"
    
    """

    @pytest.mark.exceptions
    @pytest.mark.stale_element_exception
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed(), "Instructions element should not be displayed"

    """
    
    # Open page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    # Find the instructions text element
    instructions_element = driver.find_element(By.ID, "instructions")
    instructions_element._is_displayed()

    # Push add button
    add_btn_locator = driver.find_element(By.ID, "add_btn")
    add_btn_locator.click()

    # Verify instruction text element is no longer displayed
    # assert instructions_element.is_displayed(), "instructions element is not found"
    wait = WebDriverWait(driver, 10)
    assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")),
                      "Instructions element should not be displayed")

"""

    @pytest.mark.exceptions
    @pytest.mark.timeout_exception
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row2 input should be displayed, but it's not"

        """
        # Open the URL
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click on add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 2)
        row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
                                        "Failed waiting for row 2 input")

        # Verify second input field is displayed
        assert row2_input_element.is_displayed(), "Row2 input should be displayed but its not"
        """
