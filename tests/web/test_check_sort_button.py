from web_and_mobile_pikabu_tests.pages.main_page import main_page
import allure
import pytest


@allure.epic('Sorting')
@allure.story('Sort by subs')
@allure.feature('Sort')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('CLick sort')
def test_checking_auth_options():
    main_page.open()
    main_page.clicking_community_button()
    main_page.click_sort_button()
    main_page.click_sort_by_subs()
    main_page.check_sort()