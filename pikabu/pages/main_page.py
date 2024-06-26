from selene import browser, have, be
import allure
from selenium.webdriver.common.by import By


class MainPage:
    def open(self):
        with allure.step('Open browser'):
            browser.open('')
            return self

    def clicking_community_button(self):
        with allure.step('Click community button'):
            browser.element('[id="menu-communities"]').click()

    def click_sort_button(self):
        with allure.step('Click sort button'):
            browser.element('[data-role="sort"]').click()

    def click_sort_by_subs(self):
        with allure.step('Click sort by subs'):
            browser.element('.form__field:nth-child(3)').click()

    def check_sort(self):
        browser.element('[data-role="sort"]').should(have.text('по подписчикам'))

    def check_auth_yandex(self):
        with allure.step('Check auth with yandex'):
            browser.element('[data-role="ya"]').should(have.text('Войти с Яндекс ID'))

    def check_auth_vk(self):
        with allure.step('Check auth with vk'):
            browser.element('[data-role="vk"]').should(have.text('Войти через VK ID'))

    def check_auth_google(self):
        with allure.step('Check auth with google'):
            browser.element('[data-role="google"]').should(have.text('Войти через Google'))

    def search_articles(self):
        with allure.step('Input article name and press enter'):
            browser.element('.header-right-menu__search').click()
            browser.element('[name="q"]').type('Мемы').press_enter()

    def check_articles(self):
        with allure.step('Check found articles'):
            browser.element('[value="Мемы"]').should(be.visible)

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
