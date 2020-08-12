import pytest
import time
from selenium import webdriver
from web.element.gmail_element import *
from web.page.gmail import GmailPage, GmailResultPage


EMAIL = "louiske.testing@gmail.com"
PASSWORD = "appier@123"


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


def test_send_mail_and_move_to_trash(driver):
    # driver = open_browser
    test_subject = 'Hello_{}'.format(str(int(time.time())))

    gmail_main_page = GmailPage(driver)
    gmail_login_page = GmailLoginPage(driver)

    gmail_main_page.load()
    assert driver.current_url == gmail_main_page.URL

    gmail_login_page.login(EMAIL, PASSWORD)
    assert driver.current_url == gmail_main_page.INBOX_URL

    gmail_main_page.send_email(recipients=EMAIL,
                               subject=test_subject,
                               body_text='Word')

    result = GmailResultPage(driver)
    assert result.get_popup_message(SENT_POPUP_MSG)
    assert result.get_cur_latest_mail().text == test_subject

    gmail_main_page.move_mail_to_trash()
    assert result.get_popup_message(BIN_POPUP_MSG)

    gmail_main_page.open_trash()
    assert driver.current_url == gmail_main_page.TRASH_URL
    assert result.get_cur_latest_mail().text == test_subject
