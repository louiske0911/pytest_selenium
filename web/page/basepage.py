from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def input_text(self, locator, input_text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(input_text)
        return element

    def scroll_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        element.location_once_scrolled_into_view
        return element
