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
            browser.element('[data-feed-key="companies"]').click()

    def check_community_section(self, data_section):
        with allure.step('Checking community section'):
            browser.element('.company-blogs-info__title').should(have.text(data_section.community))

    def check_return_to_main(self, data_section):
        with allure.step('Checking return to main'):
            browser.element('.feed-notify').should(have.text(data_section.hot))

    def add_article(self):
        with allure.step('Click add article button'):
            browser.element('.button_add').click()
    def check_notification(self):
        with allure.step('Checking notification'):
            browser.element('.auth__notice').should(have.text('Необходимо войти или зарегистрироваться'))


main_page = MainPage()
