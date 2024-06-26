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
    main_page.clicking_community_button()
    main_page.click_sort_button()
    main_page.click_sort_by_subs()
    main_page.check_sort()