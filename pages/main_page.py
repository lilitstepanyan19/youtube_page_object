from pages.base_page import BasePage
from .locators import MainPageLocators
import time

class MainPage(BasePage):
    def search_value(self, value):
        search_input = self.browser.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(value)

    def should_be_search_value(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_INPUT), 'No search input'

    def should_not_be_search_value(self):
        assert self.is_not_element_present(*MainPageLocators.SEARCH_INPUT), 'Search input was'

    def should_be_search_btn(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_BTN), 'Search button not found'
        
    def should_not_be_search_btn(self):
        assert self.is_not_element_present(*MainPageLocators.SEARCH_BTN), 'Search button was'
        
    def search_btn_click(self):
        search_btn = self.browser.find_element(*MainPageLocators.SEARCH_BTN)
        search_btn.click()
        # time.sleep(10)

