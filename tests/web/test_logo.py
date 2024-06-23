from test_data.data import data_section
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
def test_clicking_logo():
    main_page.open()
    main_page.click_community_section()
    main_page.check_community_section(data_section)
    main_page.clicking_logo()
    main_page.check_return_to_main(data_section)

