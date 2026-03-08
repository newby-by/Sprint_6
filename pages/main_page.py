from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


class MainPage(BasePage):
    FAQs = (By.XPATH, ".//div[@class='accordion__item']")
    QUESTION = lambda number: (By.XPATH, f".//div[@id='accordion__heading-{number}']")
    ANSWER = lambda number: (By.XPATH, f".//div[@id='accordion__panel-{number}']")

    
    def has_expected_title(self):
        return self.driver.title == data.MainPageData.MAIN_PAGE_TITLE
    
    def get_question_form_FAQ_by_number(self, number):
        return self.wait_element_located(MainPage.QUESTION(number)).text

    def get_answer_form_FAQ_by_number(self, number):
        return self.wait_element_located(MainPage.ANSWER(number)).text
    
    def is_not_hidden_answer(self, number):
        return self.is_not_hidden(MainPage.ANSWER(number)) is None
