from web_and_mobile_pikabu_tests.pages.main_page import main_page
import allure
import pytest


@allure.epic('Auth')
@allure.story('Auth options')
@allure.feature('Auth')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Check auth')
def test_checking_auth_options():
    main_page.open()
    main_page.check_auth_yandex()
    main_page.check_auth_vk()
    main_page.check_auth_google()
