import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default='en', help='Choose your language:')

@pytest.fixture(scope='function')
def browser(request):
    browser = None
    user_language = request.config.getoption('lang')

    options = Options()

    # options.add_argument('headless')
    # options.add_argument('window_size = 1920 x 935')

    options.add_experimental_option('prefs', {'intl.accept_language' : user_language})

    if user_language:
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('Enter your language: ')
    yield browser
    browser.quit()










