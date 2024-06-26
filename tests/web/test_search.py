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
    main_page.search_articles()
    main_page.check_articles()