import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import data
from pages.main_page import MainPage


# conftest.py
def pytest_addoption(parser):
    parser.addoption("--br",
                     action="store",
                     default="chrome",
                     help=("The key to choose a browser: "
                           "chrome or firefox (default: chrome)"))


@pytest.fixture(scope='function')
def driver(pytestconfig):
    if pytestconfig.getoption("br") == "gecko":
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open(data.BASE_URL)
    return main_page
