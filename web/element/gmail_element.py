# Login Page
EMAIL_INPUT_XPATH = "//input[@type='email']"
PASSWORD_INPUT_XPATH = "//input[@type='password']"
NEXT_BUTTON_XPATH = "//button[contains(., '繼續')]"

COMPOSE_BUTTON_XPATH = "//div[text()='Compose']"
RECIPIENTS_INPUT_XPATH = "//textarea[@aria-label='To']"
SUBJECT_INPUT_XPATH = "//input[@aria-label='Subject']"
MSG_BODY_XPATH = "//div[@aria-label='Message Body']"
SEND_BUTTON_XPATH = "//div[text()='Send']"

# Inbox
MAIN_BOX_XPATH = "//div[@role='main']"
LATEST_MAIL_SUBJECT_XPATH = "(//div[@role='main']//span[@class='bog'])[1]"
SELECT_XPATH = "//td[@data-tooltip='Select']"

# Navigation Bar
BIN_BUTTON_XPATH = "//*[@id=':4']/div/div[1]/div[1]/div/div/div[2]/div[3]"
MORE_NAVIGATION_XPATH = "//div[@role='navigation']//*[text()='More']"
BIN_NAVIGATION_XPATH = "//span/a[@aria-label='Bin']"
LAST_NAVIGATION_XPATH = "(//div[@role='navigation']/div/div[3]/div/div/div/div)[last()]"

# Popup Message
POPUP_MSG_XPATH = "//div[@role='alert' and @aria-live='assertive']"
BIN_POPUP_MSG = "Conversation moved to Bin."
SENT_POPUP_MSG = "Message sent."
