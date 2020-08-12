from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

xpath_mail_select = "//tr[contains(.,'Hello')]//td[@data-tooltip='Select']"
xpath_mail_select_latest = "({})[1]".format(xpath_mail_select)


class GmailLocator(object):
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(., '繼續')]")
    COMPOSE_BUTTON = (By.XPATH, "//div[text()='Compose']")

    RECIPIENTS_INPUT = (By.XPATH, "//textarea[@aria-label='To']")
    SUBJECT_INPUT = (By.XPATH, "//input[@aria-label='Subject']")
    MSG_BODY = (By.XPATH, "//div[@aria-label='Message Body']")
    SEND_BUTTON = (By.XPATH, "//div[text()='Send']")

    MAIL_SUBJECT = (By.XPATH, "//tr[contains(.,'Hello')]")
    MAIL_SUBJECT_SELECT = (
        By.XPATH, "//tr[contains(.,'Hello')]//td[@data-tooltip='Select']")

    BIN_BUTTON = (
        By.XPATH, "//*[@id=':4']/div/div[1]/div[1]/div/div/div[2]/div[3]")
    MORE_NAVIGATION = (By.XPATH, "//div[@role='navigation']//*[text()='More']")
    BIN_NAVIGATION = (By.XPATH, "//span/a[@aria-label='Bin']")

    BIN_POPUP_MSG = "Conversation moved to Bin."
    SENT_POPUP_MSG = "Message sent."


class GmailPage(object):
    URL = "https://mail.google.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.URL)

    def input_email(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable(GmailLocator.EMAIL_INPUT))
        element.send_keys(text)

    def input_passwrod(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable(GmailLocator.PASSWORD_INPUT))
        element.send_keys(text)

    def click_next_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(GmailLocator.NEXT_BUTTON))
        element.click()

    def click_compose_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(GmailLocator.COMPOSE_BUTTON))
        element.click()

    def input_recipients(self, mail):
        self.driver.find_element(
            *GmailLocator.RECIPIENTS_INPUT).send_keys(mail)
        print(*GmailLocator.RECIPIENTS_INPUT)

    def input_subject(self, text):
        self.driver.find_element(
            *GmailLocator.SUBJECT_INPUT).send_keys(text)

    def input_message_box(self, text):
        self.driver.find_element(
            *GmailLocator.MSG_BODY).send_keys(text)

    def click_send_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(GmailLocator.SEND_BUTTON))
        element.click()

    def select_subject(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_mail_select)))
        element.click()

    def select_latest_subject(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_mail_select_latest)))
        element.click()

    def click_bin_button(self):
        self.wait.until(
            lambda driver: self.driver.find_element(*GmailLocator.BIN_BUTTON))
        self.driver.find_element(*GmailLocator.BIN_BUTTON).click()

    def click_more_span(self):
        element = self.driver.find_element(*GmailLocator.MORE_NAVIGATION)
        element.location_once_scrolled_into_view
        self.wait.until(
            lambda driver: self.driver.find_element(*GmailLocator.MORE_NAVIGATION))
        self.driver.find_element(*GmailLocator.MORE_NAVIGATION).click()

    def click_bin_span(self):
        element = self.driver.find_element_by_xpath(
            "(//div[@role='navigation']/div/div[3]/div/div/div/div)[last()]")
        element.location_once_scrolled_into_view
        element = self.wait.until(
            EC.element_to_be_clickable(GmailLocator.BIN_NAVIGATION))
        element.click()

    def wait_until_msg(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='alert' and @aria-live='assertive'][contains(.,'" + text + "')]")))
        return element.text


class GmailResultPage(object):
    pass
