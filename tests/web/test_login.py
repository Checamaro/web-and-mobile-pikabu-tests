import pytest
from web_and_mobile_pikabu_tests.pages.login_page import login_page
import allure


@allure.epic('Login')
@allure.story('Correct login web_and_mobile_pikabu_tests')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
@pytest.mark.web
@pytest.mark.critical
@allure.title('Successful auth')
@pytest.mark.xfail(reason="Displaying captcha")
def test_successful_authorization():
    login_page.open()
    login_page.login_user()
    login_page.check_successful_authorization()


@allure.epic('Login')
@allure.story('Incorrect login web_and_mobile_pikabu_tests')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
@pytest.mark.web
@pytest.mark.critical
@allure.title('Unsuccessful auth')
@pytest.mark.xfail(reason="Displaying captcha")
def test_unsuccessful_login_user():
    login_page.open()
    login_page.login_user_wrong_password()
    login_page.check_unsuccessful_authorization()
