from web_and_mobile_pikabu_tests.pages.main_page import main_page
import allure
import pytest


@allure.epic('Blogs')
@allure.story('Blogs section')
@allure.feature('Blogs')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('CLick blogs')
def test_searching_articles():
    main_page.open()
    main_page.clicking_blogs_section()
    main_page.check_go_to_blogs()