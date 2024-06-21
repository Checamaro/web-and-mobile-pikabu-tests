import os
from selene import browser, have
import allure


class LoginPage:
    def open(self):
        with allure.step('Open browser'):
            browser.open('')
            return self

    def login_user(self):
        with allure.step('Input login'):
            browser.element('[value=login]').type(os.getenv('user_login_web'))
        with allure.step('Input password'):
            browser.element('[autocomplete=password]').type(os.getenv('user_password_web'))
        with allure.step('Click on submit button'):
            browser.element('.button__title').click()

    def login_user_wrong_password(self):
        with allure.step('Input login'):
            browser.element('[value=login]').type(os.getenv('asd'))
        with allure.step('Input password'):
            browser.element('[autocomplete=password]').type(os.getenv('asd'))
        with allure.step('Click on submit button'):
            browser.element('.button__title').click()

    def check_successful_authorization(self):
        with allure.step('Checking profile name'):
            browser.element('.profile__user').should(have.text('788test567'))

    def check_unsuccessful_authorization(self):
        with allure.step('Check message'):
            browser.element("//span[contains(text(), 'Ошибка. Вы ввели неверные данные авторизации')]").should(
                have.text('Ошибка. Вы ввели неверные данные авторизации'))


login_page = LoginPage()
