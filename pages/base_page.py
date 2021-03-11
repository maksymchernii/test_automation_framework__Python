from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message="Can't find element by locator {0}".format(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message="Can't find elements by locator {0}".format(locator))

    def enter_text(self, locator, text):
        search_field = self.find_element(locator)
        search_field.send_keys(text)
        return search_field

    def click_on_the_element(self, locator):
        return self.find_element(locator, time=2).click()

    def go_to_frame(self, locator):
        self.browser.switch_to.frame(locator)

    def go_to_parent_window(self):
        self.browser.switch_to.default_content()