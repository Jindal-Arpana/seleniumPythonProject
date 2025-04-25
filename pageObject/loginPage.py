from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObject.basePage import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "submit")
    __error_msg = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # self._driver = driver

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_msg(self) -> str:
        return super()._get_text(self.__error_msg, 3)



        # wait = WebDriverWait(self._driver, 10)
        #
        # wait.until(ec.visibility_of_element_located(self.__username_field))
        # self._driver.find_element(self.__username_field).send_keys(username)
        #
        # wait.until(ec.visibility_of_element_located(self.__password_field))
        # self._driver.find_element(self.__password_field).send_keys(password)
        #
        # wait.until(ec.visibility_of_element_located(self.__submit_button))
        # self._driver.find_element(self.__submit_button).click()
