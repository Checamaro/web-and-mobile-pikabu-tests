import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


def check_notification():

    with allure.step('Check notification'):
        if browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout['
                                            '@resource-id="com.android.permissioncontroller:id/content_container'
                                            '"]/android.widget.LinearLayout')).matching(be.visible):
            browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()
