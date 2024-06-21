from selene import browser, have
import allure


class MainPage:
    def open(self):
        with allure.step('Open browser'):
            browser.open('')
            return self

    def clicking_logo(self):
        with allure.step('Click logo'):
            browser.element('.header__logo').click()

    def click_community_section(self):
        with allure.step('Click communities'):
            browser.element('#menu-communities').click()

    def check_community_section(self, data):
        with allure.step('Checking community section'):
            browser.element('.menu__item_current').should(have.text(data.community))

    def check_return_to_main(self, data):
        with allure.step('Click on main logo'):
            browser.element('[pikabu-feed-key=hot]').should(have.text(data.hot))


main_page = MainPage()
