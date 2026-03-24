from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    SCOOTER_LINK = (By.XPATH, ".//a[contains(@class, 'LogoScooter')]")
    YANDEX_LINK = (By.XPATH, ".//a[contains(@class, 'LogoYandex')]")

    def go_to_main_page_scooter(self):
        self.click(HeaderPage.SCOOTER_LINK)

    def go_to_main_page_yandex(self):
        self.click(HeaderPage.YANDEX_LINK)
