import time
from web.library.decode import decode_password
from web.element.gmail_element import *
from web.page.gmail import GmailPage, GmailLoginPage, GmailResultPage


def test_send_mail_and_move_to_trash(config, open_browser):
    driver = open_browser

    # test data init
    test_subject = 'Hello_{}'.format(str(int(time.time())))
    test_email = config['EMAIL']
    test_password = decode_password(config['PASSWORD'])

    gmail_main_page = GmailPage(driver)
    gmail_login_page = GmailLoginPage(driver)

    # test step
    gmail_main_page.load()
    gmail_login_page.login(test_email, test_password)
    assert driver.current_url == gmail_main_page.INBOX_URL

    gmail_main_page.send_email(recipients=test_email,
                               subject=test_subject,
                               body_text='Word')

    result = GmailResultPage(driver)
    assert result.get_popup_message(SENT_POPUP_MSG)
    assert result.get_cur_latest_mail().text == test_subject

    gmail_main_page.move_mail_to_trash(subject=test_subject)
    assert result.get_popup_message(BIN_POPUP_MSG)

    gmail_main_page.open_trash()
    assert driver.current_url == gmail_main_page.TRASH_URL
    assert result.get_cur_latest_mail().text == test_subject
