import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic('Notifications')
@allure.story('Skip notification')
@allure.feature('Notification')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_skip_notification():
    with allure.step('Press Dont allow notifications button'):
        browser.element((AppiumBy.ID,
                         'com.android.permissioncontroller:id/permission_deny_button')).click()

    with allure.step('Checking main page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="ГОРЯЧЕЕ"]')).should(
            have.text('ГОРЯЧЕЕ'))
