import allure

import data
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.yandex_page import YandexPage


@allure.testcase(url=data.BASE_URL,
                 name='The testing of the header pages app')
class TestHeader:

    @allure.title('Test logo «Самокат»')
    @allure.description('if click on logo «Самоката» '
                        'then redirect to the main page «Самокат»')
    def test_after_click_logo_scooter_goto_main_page_scooter(self, main_page):
        header = HeaderPage(main_page.driver)
        header.go_to_main_page_scooter()

        main_page = MainPage(header.driver)

        assert main_page.has_expected_main_title()

    @allure.title('Test logo «Яндекс»')
    @allure.description('if click on logo «Яндекс» then '
                        'redirect to the main page «Яндекс»')
    def test_after_click_logo_yandex_goto_dzen(self, main_page):
        header = HeaderPage(main_page.driver)
        current_window = header.get_current_handle()
        header.go_to_main_page_yandex()

        all_windows = header.get_all_handles()
        all_windows.remove(current_window)
        header.switch_to_window(all_windows[0])

        ya_page = YandexPage(header.driver)

        assert ya_page.is_main_page_available()
