from pikabu.pages.main_page import main_page
import allure
import pytest


@allure.epic('Logo')
@allure.story('Header logo')
@allure.feature('Logo')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('CLick logo')
def test_checking_auth_options():
    main_page.open()
    main_page.check_auth_yandex()
    main_page.check_auth_vk()
    main_page.check_auth_google()
