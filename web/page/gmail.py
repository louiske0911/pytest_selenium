from web.element.gmail_element import *
from web.page.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GmailLocator(object):
    # Login Page
    EMAIL_INPUT = (By.XPATH, EMAIL_INPUT_XPATH)
    PASSWORD_INPUT = (By.XPATH, PASSWORD_INPUT_XPATH)
    NEXT_BUTTON = (By.XPATH, NEXT_BUTTON_XPATH)

    # Compose
    COMPOSE_BUTTON = (By.XPATH, COMPOSE_BUTTON_XPATH)
    RECIPIENTS_INPUT = (By.XPATH, RECIPIENTS_INPUT_XPATH)
    SUBJECT_INPUT = (By.XPATH, SUBJECT_INPUT_XPATH)
    MSG_BODY = (By.XPATH, MSG_BODY_XPATH)
    SEND_BUTTON = (By.XPATH, SEND_BUTTON_XPATH)

    # Inbox
    LATEST_MAIL_SUBJECT = (By.XPATH, LATEST_MAIL_SUBJECT_XPATH)

    # Navigation Bar
    BIN_BUTTON = (By.XPATH, BIN_BUTTON_XPATH)
    MORE_NAVIGATION = (By.XPATH, MORE_NAVIGATION_XPATH)
    BIN_NAVIGATION = (By.XPATH, BIN_NAVIGATION_XPATH)
    LAST_NAVIGATION = (By.XPATH, LAST_NAVIGATION_XPATH)

    # Popup Message
    POPUP_MSG = (By.XPATH, POPUP_MSG_XPATH)


class GmailPage(BasePage):
    URL = "https://mail.google.com/"
    INBOX_URL = URL + "mail/u/0/#inbox"
    TRASH_URL = URL + "mail/u/0/#trash"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get(self.URL)

    # compoase
    def click_compose_button(self):
        self.click(GmailLocator.COMPOSE_BUTTON)

    def input_recipients(self, recipients):
        self.input_text(GmailLocator.RECIPIENTS_INPUT, recipients)

    def input_subject(self, subject):
        self.input_text(GmailLocator.SUBJECT_INPUT, subject)

    def input_message_box(self, body_text):
        self.input_text(GmailLocator.MSG_BODY, body_text)

    def click_send_button(self):
        self.click(GmailLocator.SEND_BUTTON)

    # inbox
    def select_latest_subject(self, subject):
        subject_xpath = "{}//tr[contains(.,'{}')]{}".format(MAIN_BOX_XPATH,
                                                            subject,
                                                            SELECT_XPATH)
        subject_select = (By.XPATH, subject_xpath)
        self.click(subject_select)

    def click_bin_button(self):
        self.wait.until(
            lambda driver: self.driver.find_element(*GmailLocator.BIN_BUTTON))
        self.driver.find_element(*GmailLocator.BIN_BUTTON).click()

    # navigation bar
    def click_more_span(self):
        self.scroll_to_element(*GmailLocator.MORE_NAVIGATION)
        self.click(GmailLocator.MORE_NAVIGATION)

    def click_bin_span(self):
        self.scroll_to_element(*GmailLocator.LAST_NAVIGATION)
        self.click(GmailLocator.BIN_NAVIGATION)

    # integration keyword
    def send_email(self, recipients, subject, body_text):
        self.click_compose_button()
        self.input_recipients(recipients)
        self.input_subject(subject)
        self.input_message_box(body_text)
        self.click_send_button()

    def move_mail_to_trash(self, subject):
        self.select_latest_subject(subject)
        self.click_bin_button()

    def open_trash(self):
        self.click_more_span()
        self.click_bin_span()
        self.wait.until(EC.url_matches(self.TRASH_URL))


class GmailLoginPage(GmailPage):

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, text):
        self.input_text(GmailLocator.EMAIL_INPUT, text)

    def input_passwrod(self, text):
        self.input_text(GmailLocator.PASSWORD_INPUT, text)

    def click_next_button(self):
        self.click(GmailLocator.NEXT_BUTTON)

    def login(self, email, password):
        self.input_email(email)
        self.click_next_button()
        self.input_passwrod(password)
        self.click_next_button()
        self.wait.until(EC.url_matches(self.INBOX_URL))


class GmailResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_popup_message(self, text):
        text_popup_msg = POPUP_MSG_XPATH + "//*[text()='" + text + "']"
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, text_popup_msg)))
        return element.text == text

    def get_cur_latest_mail(self):
        element = self.wait.until(
            EC.visibility_of_element_located(GmailLocator.LATEST_MAIL_SUBJECT))
        return element
