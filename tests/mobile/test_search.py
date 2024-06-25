import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.epic('Search')
@allure.story('Search')
@allure.feature('Search')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_search_python():
    with allure.step('Close add post'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Посты"]')).should(be.visible).click()

    with allure.step('Click search button'):
        browser.element((AppiumBy.ID,
                         'ru.pikabu.android:id/action_search')).click()

    with allure.step('Type and click search'):
        browser.element((AppiumBy.ID,
                         'ru.pikabu.android:id/et_search')).type('python')
        browser.element((AppiumBy.ID, 'ru.pikabu.android:id/action_apply')).click()

    with allure.step('Checking search results'):
        browser.element((AppiumBy.ID, 'ru.pikabu.android:id/tv_text')).should(
            have.text('"python". Любые посты за все время, сортировка по релевантности, рейтинг любой'))
