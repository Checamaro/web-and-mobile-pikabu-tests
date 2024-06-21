import pytest
from pikabu.pages.login_page import login_page
import allure


@allure.epic('Login')
@allure.story('Correct login pikabu')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
@pytest.mark.web
@pytest.mark.critical
@allure.title('Successful auth')
def test_successful_authorization():
    login_page.open()
    login_page.login_user()
    login_page.check_successful_authorization()


@allure.epic('Login')
@allure.story('Incorrect login pikabu')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
@pytest.mark.web
@pytest.mark.critical
@allure.title('Unsuccessful auth')
def test_unsuccessful_login_user():
    login_page.open()
    login_page.login_user_wrong_password()
    login_page.check_unsuccessful_authorization()
