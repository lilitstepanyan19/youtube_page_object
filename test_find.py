from pages.main_page import MainPage
from pages.find_page import FindPage
from pages.write_file import WriteFile
import pytest

value = 'adele'
link = 'https://www.youtube.com'


def test_send_value(browser):
    page = MainPage(browser, link)
    page.open()
    page.search_value(value)
    page.search_btn_click()

def test_should_be_search_value(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_value()

@pytest.mark.xfail
def test_should_not_nbe_search_value(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_search_value()

def test_should_be_search_btn(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_btn()

@pytest.mark.xfail
def test_should_not_be_search_btn(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_search_btn()

@pytest.mark.result
class TestFindResult():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.search_value(value)
        page.search_btn_click()

    def test_search_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.search_result()

    def test_should_be_search_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_be_search_result()
    
    @pytest.mark.xfail
    def test_should_not_search_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_not_search_result()
    
    def test_result_list(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.result_list()
    
    def test_should_be_title_in_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_be_title_in_result()
    
    @pytest.mark.xfail
    def test_should_not_be_title_in_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_not_be_title_in_result()

    def test_should_be_view_in_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_be_view_in_result()
    
    @pytest.mark.xfail
    def test_should_not_be_view_in_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_not_be_view_in_result()

    def test_should_be_year_in_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_be_year_in_result()
    
    @pytest.mark.xfail
    def test_should_not_be_year_in_result(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        find_page.should_not_be_year_in_result()

@pytest.mark.write
class TestWriteFile():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.search_value(value)
        page.search_btn_click()

    def test_json_file(self, browser):
        find_page = FindPage(browser, browser.current_url)
        find_page.open()
        info_list = find_page.result_list()
        WriteFile.write_info_file(info_list)

    def test_should_be_json_file(self):
            WriteFile.should_be_json_file()
            
    # @pytest.mark.xfail
    def test_should_be_json_file_not_empty(self):
            WriteFile.should_be_json_file_not_empty()


