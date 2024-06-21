from test_data.data import data_search_with_filter, data_search
from pikabu.pages.search_page import search_page
import allure
import pytest


@allure.epic('Search')
@allure.story('Search python')
@allure.feature('Search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Search python')
def test_search():
    search_page.open()
    search_page.search_python(data_search)
    search_page.successful_search_pyhton(data_search)


@allure.epic('Search')
@allure.story('Search with filter')
@allure.feature('Search with filter')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Search with filter')
def test_search_with_filter():
    search_page.open()
    search_page.search_by_filter_tag(data_search_with_filter)
    search_page.check_search_by_filter_tag(data_search_with_filter)

