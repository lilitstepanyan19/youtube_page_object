from pages.base_page import BasePage
from .locators import FindPageLocators
import cgitb

class FindPage(BasePage):
    def search_result(self):
        search_result = self.browser.find_elements(*FindPageLocators.SEARCH_RESULT)
        return search_result
        
    def result_list(self):
        adele_list = []
        for i in range(0, 5):
            info_list = {}
            info_list['title'] = self.search_result()[i].find_element(*FindPageLocators.TITLE).text
            info_list['view'] = self.search_result()[i].find_element(*FindPageLocators.VIEW).text
            info_list['year'] = self.search_result()[i].find_element(*FindPageLocators.YEAR).text
            adele_list.append(info_list)
        print(adele_list)
