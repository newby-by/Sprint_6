from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class YandexPage(BasePage):
    SEARCH_INPUT = (By.XPATH, ".//form[@action='https://yandex.ru/search/']")

    def is_main_page_available(self):
        return self.wait_element_located(YandexPage.SEARCH_INPUT)
