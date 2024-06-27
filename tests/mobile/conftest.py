import allure
import pytest
from selene import browser
from appium import webdriver
from web_and_mobile_pikabu_tests.utils import attach
from web_and_mobile_pikabu_tests.activity import start_activity
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def handle_notifications():
    with allure.step('Check for notification and close if present'):
        start_activity.check_notification()


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption('--context')
    load_dotenv(dotenv_path=f'.env.{context}')


@pytest.fixture
def context(request):
    return request.config.getoption('--context')


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import config
    options = config.to_driver_options(context=context)

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            options.get_capability('remote_url'),
            options=options
        )

    browser.config.timeout = 10.0

    yield

    attach.screenshot()

    attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id' + session_id):
        browser.quit()

    if context == 'bstack':
        attach.bstack_video(session_id)
