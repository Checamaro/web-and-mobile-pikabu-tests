import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.epic('Notifications')
@allure.story('Skip notification')
@allure.feature('Notification')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_filtration_by_tag():
    with allure.step('Close add post'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Посты"]')).should(be.visible).click()

    with allure.step('Press menu button'):
        browser.element((AppiumBy.XPATH,
                         '//android.view.ViewGroup[@resource-id="ru.pikabu.android:id/toolbar"]/android.widget'
                         '.ImageButton')).click()

    with allure.step('Click tags tab'):
        browser.element((AppiumBy.XPATH, '//android.widget.CheckedTextView['
                                         '@resource-id="ru.pikabu.android:id/design_menu_item_text" and '
                                         '@text="Теги"]')).click()

    with allure.step('Checking tags'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="ВСЕ ТЕГИ"]')).should(
            have.text('ВСЕ ТЕГИ'))

    with allure.step('Filtering tags by "Юмор"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.pikabu.android:id/tv_name" and '
                                         '@text="Юмор"]')).click()

    with allure.step('Checking search results by tag "Юмор"'):
        browser.element((AppiumBy.ID, 'ru.pikabu.android:id/tv_text')).should(
            have.text('Юмор\nЛюбые посты за все время, сортировка cвежее, рейтинг любой'))
