from pages.base_page import BasePage
from .locators import FindPageLocators
from cgitb import text

class FindPage(BasePage):
    def search_result(self):
        search_result = self.browser.find_elements(*FindPageLocators.SEARCH_RESULT)
        return search_result
    
    def should_be_search_result(self):
        assert self.search_result(), 'Nothing finded'

    def should_not_search_result(self):
        assert not self.search_result(), 'Search result finded'
        
    def result_list(self):
        adele_list = []
        for i in range(0, 5):
            info_list = {}
            info_list['title'] = self.search_result()[i].find_element(*FindPageLocators.TITLE).text
            info_list['view'] = self.search_result()[i].find_element(*FindPageLocators.VIEW).text
            info_list['year'] = self.search_result()[i].find_element(*FindPageLocators.YEAR).text
            adele_list.append(info_list)
        return adele_list

    def should_be_title_in_result(self):
        assert self.is_element_present(*FindPageLocators.TITLE), 'This title not found'

    def should_not_be_title_in_result(self):
        assert self.is_not_element_present(*FindPageLocators.TITLE), 'This title right'

    def should_be_view_in_result(self):
        assert self.is_element_present(*FindPageLocators.VIEW), 'This view not found'

    def should_not_be_view_in_result(self):
        assert self.is_not_element_present(*FindPageLocators.VIEW), 'This view right'

    def should_be_year_in_result(self):
        assert self.is_element_present(*FindPageLocators.YEAR), 'This year not found'

    def should_not_be_year_in_result(self):
        assert self.is_not_element_present(*FindPageLocators.YEAR), 'This year right'










