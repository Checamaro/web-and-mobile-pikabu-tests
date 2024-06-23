from pikabu.pages.main_page import main_page
import allure
import pytest


@allure.epic('Add article')
@allure.story('Add article')
@allure.feature('Add article')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Add article')
def test_adding_article():
    main_page.open()
    main_page.add_article()
    main_page.check_notification()





