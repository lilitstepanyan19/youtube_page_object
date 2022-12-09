from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except SyntaxError:
            return False
        return True
    
    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, timeout=4).until(EC.presence_of_element_located((how, what)))
        except TimeoutError:
            return True
        return False
        











