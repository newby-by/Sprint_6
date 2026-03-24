from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class StatusPage(BasePage):
    SEE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Посмотреть']")
    ORDER_DATA = (By.XPATH, ".//*[contains(@class, 'Track_Row')]")
    ORDER_DATA_TITLE = (By.XPATH, ".//*[contains(@class, 'Track_Title')]")
    ORDER_DATA_VALUE = (By.XPATH, ".//*[contains(@class, 'Track_Value')]")

    def has_button_see_order(self):
        return self.wait_element_clickable(StatusPage.SEE_ORDER_BUTTON)

    def get_number_fields_on_page(self):
        self.wait_element_located(StatusPage.ORDER_DATA)

        return len(self.driver.find_elements(*StatusPage.ORDER_DATA))
