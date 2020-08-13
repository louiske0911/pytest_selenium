import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope='session')
def config():
    with open('conf/setting.yaml') as yaml_file:
        data = yaml.safe_load(yaml_file)

    env = data['common']['ENV']
    config = data['common']
    if data[env]:
        config.update(data[env])
    return config


@pytest.fixture(scope="function")
def open_browser(config, request):
    browser = config['BROWSER']

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
        raise Exception(f'"{browser}" is not a supported browser')

    driver.implicitly_wait(config['DEFAULT_WAIT'])
    driver.set_window_size(1920, 1080)

    yield driver  # Teardown
    driver.close()
    driver.quit()
