from abc import ABC

import allure


class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open the page with {url}")
    def open(self, url):
        self.driver.get(url)
