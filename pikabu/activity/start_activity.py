import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def check_notification():

    with allure.step('Check notification'):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_message')).should(have.text('Allow Pikabu to send you notifications?'))
def close_notification():

    with allure.step('Close notification'):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()