from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import data
from pages.base_page import BasePage


class OrderScooter(BasePage):
    COOKIE_WINDOW = (By.XPATH,
                     ".//div[contains(@class, 'App_CookieConsent')]")
    ORDER_FIELD = lambda number: (By.XPATH,
                                  ("(.//div[contains(@class, "
                                   f"'Order_Content')]//input)[{number}]"))
    FIRST_SELECT = (By.XPATH,
                    ("(.//li[contains(@class, "
                     "'select-search')]/button)[1]"))
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DATE_FIELD = (By.XPATH,
                  ".//div[contains(@class, 'react-datepicker')]/input")
    RENTAL_PERIOD_FIELD = (By.XPATH,
                           ".//div[contains(@class, 'Dropdown-root')]")
    RENTAL_PERIOD_VALUE = lambda number: (By.XPATH,
                                          "(.//div[contains(@class, "
                                          f"'Dropdown-option')])[{number}]")
    SCOOTER_COLOR = lambda number: (By.XPATH,
                                    ("(.//div[text()='Цвет самоката']"
                                     "/following-sibling::*//input)"
                                     f"[{number}]"))
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    COMMENTS_FIELD = (
        By.XPATH,
        ".//input[contains(@placeholder, 'Комментарий для курьера')]"
    )
    ORDER_BUTTON_IN_FORM = (By.XPATH, "(.//button[text()='Заказать'])[2]")
    SUBMIT_ORDER = (By.XPATH, ".//button[text()='Да']")
    ORDER_PLACED = (By.XPATH, ".//div[text()='Заказ оформлен']")
    SEE_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")
    NUMBER_ORDER = (By.XPATH, ".//div[contains(text(), 'Номер заказа: ')]")

    @classmethod
    def order_number(cls, row_message):
        return row_message.split(':')[1].split('.')[0].strip()

    @step("Номер заказа")
    def get_order_number(self):
        self.wait_text_in_element(
            OrderScooter.NUMBER_ORDER, OrderScooter.order_number
        )

        return OrderScooter.order_number(
            self.driver.find_element(*OrderScooter.NUMBER_ORDER).text
        )

    @step("Заполнение поля \"Имя\" значением {first_name}")
    def set_field_first_name(self, first_name):
        self.wait_element_located(
            OrderScooter.ORDER_FIELD(data.OrderScooterForm.FIELDS['Имя'])
        ).send_keys(first_name)

    @step("Заполнение поля \"Фамилия\" значением {last_name}")
    def set_field_last_name(self, last_name):
        self.wait_element_located(
            OrderScooter.ORDER_FIELD(data.OrderScooterForm.FIELDS['Фамилия'])
        ).send_keys(last_name)

    @step("Заполнение поля \"Метро\" значением {metro_name}")
    def set_field_metro(self, metro_name):
        self.wait_element_located(
            OrderScooter.ORDER_FIELD(
                data.OrderScooterForm.FIELDS['Станция метро']
            )
        ).send_keys(metro_name)

        self.click(OrderScooter.FIRST_SELECT)

    @step("Заполнение поля \"Адрес\" значением {address}")
    def set_field_address(self, address):
        self.wait_element_located(
            OrderScooter.ORDER_FIELD(data.OrderScooterForm.FIELDS['Адрес'])
        ).send_keys(address)

    @step("Заполнение поля \"Телефон\" значением {phone_number}")
    def set_field_phone_number(self, phone_number):
        self.wait_element_located(
            OrderScooter.ORDER_FIELD(data.OrderScooterForm.FIELDS['Телефон'])
        ).send_keys(phone_number)

    @step("Переход к следующей части формы")
    def press_next_to_order(self):
        self.click(OrderScooter.NEXT_BUTTON)

    @step("Заполнение поля \"Дата\" значением {date_of_pick_up}")
    def set_field_date_of_pick_up(self, date_of_pick_up):
        element = self.wait_element_located(OrderScooter.DATE_FIELD)
        element.send_keys(date_of_pick_up)
        element.send_keys(Keys.ENTER)

    @step("Заполнение поля \"Период аренды\" значением {rental_period_date}")
    def set_rental_period(self, rental_period_date):
        self.wait_element_located(OrderScooter.RENTAL_PERIOD_FIELD).click()
        self.wait_element_located(
            OrderScooter.RENTAL_PERIOD_VALUE(
                data.OrderScooterForm.RENTAL_PERIOD[rental_period_date]
            )
        ).click()

    @step("Заполнение поля \"Цвет скутера\" значением {color}")
    def set_scooter_color(self, color):
        self.wait_element_clickable(
            OrderScooter.SCOOTER_COLOR(
                data.OrderScooterForm.SCOOTER_COLOR[color])
        ).click()

    @step("Заполнение поля \"Комментарий для курьера\" значением {comment}")
    def set_comments_for_courier(self, comment):
        self.wait_element_located(
            OrderScooter.COMMENTS_FIELD).send_keys(comment)

    @step("Нажимаем кнопку \"Заказать\"")
    def order_scooter(self):
        self.wait_element_clickable(OrderScooter.ORDER_BUTTON_IN_FORM)
        btn = self.driver.find_element(*OrderScooter.ORDER_BUTTON_IN_FORM)
        btn.click()

    @step("Подтверждаем заказ \"Да\"")
    def submit_order(self):
        self.wait_element_clickable(OrderScooter.SUBMIT_ORDER)
        btn = self.driver.find_element(*OrderScooter.SUBMIT_ORDER)
        btn.click()

    @step("Посмотреть статус")
    def see_status(self):
        self.wait_element_clickable(OrderScooter.SEE_STATUS_BUTTON)
        btn = self.driver.find_element(*OrderScooter.SEE_STATUS_BUTTON)
        btn.click()

    def has_comment_about_successfully_placed(self):
        return self.wait_element_located(OrderScooter.ORDER_PLACED)

    def has_order_number(self):
        return self.wait_text_in_element(
            OrderScooter.NUMBER_ORDER,
            OrderScooter.order_number
        )

    @step("Заполнение формы заказа")
    def fill_form(self, form_data):
        self.remove_cookie_window(OrderScooter.COOKIE_WINDOW)
        self.set_field_first_name(form_data.first_name)
        self.set_field_last_name(form_data.last_name)
        self.set_field_address(form_data.address)
        self.set_field_metro(form_data.metro)
        self.set_field_phone_number(form_data.phone_number)
        self.press_next_to_order()

        self.set_field_date_of_pick_up(form_data.date_of_pick_up)
        self.set_rental_period(form_data.rental_period)
        self.set_scooter_color(form_data.scooter_color)
        self.set_comments_for_courier(form_data.comments_for_courier)
