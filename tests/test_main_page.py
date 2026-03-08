import allure

import data
from pages.main_page import MainPage


@allure.testcase(url=data.BASE_URL, name='The testing of the main page app')
class TestsMainPage:

    @allure.title('The main page is available')
    @allure.description('We check available start page of app by a page title')
    def test_main_page_is_available(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        assert main_page.has_expected_title()
