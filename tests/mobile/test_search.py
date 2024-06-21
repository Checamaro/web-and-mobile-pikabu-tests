import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic('Search')
@allure.story('Search')
@allure.feature('Search')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_search_pyhton():
    with allure.step('Click search button'):
        browser.element((AppiumBy.ID,
                         'ru.pikabu.android:id/action_search')).click()

    with allure.step('Click search'):
        browser.element((AppiumBy.ID,
                         'ru.pikabu.android:id/et_search')).type('python').press_enter()

    with allure.step('Checking search results'):
        browser.element((AppiumBy.ID, 'ru.pikabu.android:id/tv_text')).should(
            have.text('"python". Любые посты за все время, сортировка по релевантности, рейтинг любой'))

