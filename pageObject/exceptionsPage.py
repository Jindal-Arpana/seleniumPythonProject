from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObject.basePage import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __error_msg = (By.ID, "error")
    __add_button_locator = (By.ID, "add_btn")
    __row1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __row1_save_button_element = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row2_save_button_element = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_msg_element = (By.ID, "confirmation")
    __row1_edit_button_element = (By.XPATH, "//div[@id='row1']/button[@name='Edit']")
    __pizza_element = (By.XPATH, "//input[@type='text' and @value='Pizza']")
    __instructions_element = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_button(self):
        super()._click(self.__add_button_locator)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row2_input_element)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__row2_input_element)

    def add_second_food(self, food: str):
        super()._type(self.__row2_input_element, food)
        super()._click(self.__row2_save_button_element)
        super()._wait_until_element_is_visible(self.__confirmation_msg_element)

    def get_confirmation_message(self) -> str:
        return super()._get_text(self.__confirmation_msg_element, time=3)

    def modify_row_1_input(self, food: str):
        super()._click(self.__row1_edit_button_element)
        super()._wait_until_element_is_clickable(self.__pizza_element)
        super()._clear(self.__pizza_element)
        super()._type(self.__pizza_element, food)
        super()._click(self.__row1_save_button_element)
        super()._wait_until_element_is_visible(self.__confirmation_msg_element)

    def are_instructions_displayed(self) -> bool:
        return super()._is_displayed(self.__instructions_element)

