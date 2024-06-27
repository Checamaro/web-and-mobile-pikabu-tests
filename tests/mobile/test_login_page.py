import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.epic('Authorization')
@allure.story('Authorization')
@allure.feature('Authorization')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_authorization_user():

    with allure.step('Close add post'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Посты"]')).should(be.visible).click()

    with allure.step('Press menu button'):
        browser.element((AppiumBy.XPATH,
                         '//android.view.ViewGroup[@resource-id="ru.web_and_mobile_pikabu_tests.android:id/toolbar"]/android.widget'
                         '.ImageButton')).click()

    with allure.step('Press login button'):
        browser.element((AppiumBy.ID,
                         'ru.web_and_mobile_pikabu_tests.android:id/iv_login')).click()

    with allure.step('Checking login'):
        browser.element((AppiumBy.ID, 'ru.web_and_mobile_pikabu_tests.android:id/login')).should(
            have.text('Логин, email или телефон'))

    with allure.step('Checking password'):
        browser.element((AppiumBy.ID, 'ru.web_and_mobile_pikabu_tests.android:id/password')).should(
            have.text('Пароль'))

    with allure.step('Checking Auth button'):
        browser.element((AppiumBy.ID, 'ru.web_and_mobile_pikabu_tests.android:id/loginBtn')).should(
            have.text('Войти'))
