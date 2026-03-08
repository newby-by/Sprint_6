import allure
import pytest

import data
from pages.main_page import MainPage


@allure.testcase(url=data.BASE_URL, name='The testing of the main page app')
class TestsMainPage:

    @allure.title('The main page is available')
    @allure.description('We check available start '
                        'page of app by a page title')
    def test_main_page_is_available(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        assert main_page.has_expected_title()

    @allure.title('The faq accordion with clickable elements')
    @allure.description('We check dropdown by click on answer '
                        'element and an answer is correct')
    @pytest.mark.parametrize('number',
                             range(len(data.MainPageData.FAQAccordion.FAQ)))
    def test_FAQs_accordion_click_to_question_open_with_correct_answer(
        self, driver, number
    ):
        main_page = MainPage(driver)
        
        main_page.open(data.BASE_URL)

        main_page.scroll_to(MainPage.QUESTION(number))
        main_page.click(MainPage.QUESTION(number))
       
        with allure.step('Get a question and an answer'):
            question = main_page.get_question_form_FAQ_by_number(number)
            answer = main_page.get_answer_form_FAQ_by_number(number)

        with allure.step('Checking'):
            assert (main_page.is_not_hidden_answer(number) and
                    data.MainPageData.FAQAccordion.FAQ[question] == answer)
