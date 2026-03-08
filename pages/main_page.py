import data
from pages.base_page import BasePage


class MainPage(BasePage):
    
    def has_expected_title(self):
        return self.driver.title == data.MAIN_PAGE_TITLE
