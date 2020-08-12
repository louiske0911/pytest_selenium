import pytest
import time
from web.page.gmail import GmailLocator, GmailPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


email = "louiske.testing@gmail.com"
password = "appier@123"


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--driver")

    if browser == 'chrome':
        chrome_driver = "./web/driver/chromedriver_83"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=en-US')
        prefs = {
            'intl.accept_languages': 'en_US'
        }
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            executable_path=chrome_driver,
            options=chrome_options)
    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    # driver.maximize_window()3
    driver.set_window_size(800, 600)
    driver.set_window_position(90, 90)

    yield driver  # Teardown
    driver.close()
    driver.quit()


def test_gmail(driver):
    # driver = open_browser

    gmail_page = GmailPage(driver)

    gmail_page.load()
    gmail_page.input_email(email)
    gmail_page.click_next_button()
    gmail_page.input_passwrod(password)
    gmail_page.click_next_button()

    gmail_page.click_compose_button()
    gmail_page.input_recipients(email)
    gmail_page.input_subject('Hello')
    gmail_page.input_message_box('Word')
    gmail_page.click_send_button()

    text = gmail_page.wait_until_msg(GmailLocator.SENT_POPUP_MSG)
    assert 'Message sent.' in text

    gmail_page.select_latest_subject()

    gmail_page.click_bin_button()
    text = gmail_page.wait_until_msg(GmailLocator.BIN_POPUP_MSG)

    assert 'Conversation moved to Bin.' in text

    gmail_page.click_more_span()
    gmail_page.click_bin_span()

    time.sleep(2)
    print(len(driver.find_elements_by_xpath(
        "//div[@id=':1']//div[@role='main']//tr[contains(.,'Hello')]")))
    assert len(driver.find_elements_by_xpath(
        "//div[@id=':1']//div[@role='main']//tr[contains(.,'Hello')]"))
