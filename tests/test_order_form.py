import allure
import pytest

import data
from pages.main_page import MainPage
from pages.order_scooter_form import OrderScooter
from pages.status_page import StatusPage


@allure.testcase(
    url=data.ORDER_FORM_URL,
    name='The testing of the form of ordering a scooter')
class TestOrderForm:

    @pytest.mark.parametrize('button', [1, 2])
    def test_status_page_has_order_form_data(self, driver, button):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        main_page.go_to_order_scooter(button)

        order_page = OrderScooter(main_page.driver)
        order_page.fill_form(data.form_data)
        order_page.order_scooter()
        order_page.submit_order()
        order_page.get_order_number()
        order_page.see_status()

        status_page = StatusPage(order_page.driver)

        assert status_page.get_number_fields_on_page() == 9
