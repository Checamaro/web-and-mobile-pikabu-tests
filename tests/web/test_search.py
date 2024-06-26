from pikabu.pages.main_page import main_page
import allure
import pytest


@allure.epic('Articles')
@allure.story('Searching articles')
@allure.feature('Articles')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('CLick articles')
def test_searching_articles():
    main_page.open()
    main_page.search_articles()
    main_page.check_articles()