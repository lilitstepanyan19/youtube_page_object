from selenium.webdriver.common.by import By

class MainPageLocators():
    SEARCH_INPUT = (By.XPATH, '//input[@id="search"]')
    SEARCH_BTN = (By.XPATH, '//button[@id="search-icon-legacy"]')

class FindPageLocators():
    SEARCH_RESULT = (By.CSS_SELECTOR, '#contents.style-scope ytd-item-section-renderer>#contents>.style-scope.ytd-item-section-renderer')
    TITLE = (By.CSS_SELECTOR, '#title-wrapper>.title-and-badge.style-scope.ytd-video-renderer')
    VIEW = (By.CSS_SELECTOR, '#metadata-line>.style-scope.ytd-video-meta-block:nth-child(1)')
    YEAR = (By.CSS_SELECTOR, '#metadata-line>.style-scope.ytd-video-meta-block:nth-child(2)')





