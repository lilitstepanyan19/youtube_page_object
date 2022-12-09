from pages.main_page import MainPage
from pages.find_page import FindPage
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

def test_search_result(browser):
    page = MainPage(browser, link)
    page.open()
    page.search_value(value)
    page.search_btn_click()
    find_page = FindPage(browser, browser.current_url)
    find_page.open()
    find_page.search_result()
    find_page.result_list()
