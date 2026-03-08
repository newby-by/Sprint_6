from abc import ABC

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable
)


class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open the page with {url}")
    def open(self, url):
        self.driver.get(url)

    def wait_element_located(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            presence_of_element_located(locator)
        )
        return element

    def wait_element_clickable(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            element_to_be_clickable(locator)
        )
        return element
    
    @allure.step("Click on an element")
    def click(self, locator):
        self.wait_element_clickable(locator).click() 

    def get_attribute(self, locator, name):
        return self.wait_element_located(locator).get_attribute(name)
    
    def is_not_hidden(self, locator):
        return self.wait_element_located(locator).get_attribute('hidden')
    
    @allure.step("Scroll to an element")
    def scroll_to(self, locator):
        element = self.wait_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)
