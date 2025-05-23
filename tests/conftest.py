import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" This statement is used to run the tests in multiple browsers """


# @pytest.fixture(params=["chrome", "firefox"])


@pytest.fixture(params=["chrome"])
def driver(request):
    # browser = request.config.getoption("--browser")
    browser = request.param
    print(f"Creating the {browser} driver")

    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"expected 'chrome' or 'firefox', but got {browser}")
    # my_driver = webdriver.Chrome()
    # my_driver = webdriver.Firefox()

    my_driver.maximize_window()
    my_driver.implicitly_wait(10)

    yield my_driver
    print(f"\nClosing the {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
