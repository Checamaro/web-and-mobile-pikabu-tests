from selene import browser, have
import allure


class SearchPage:
    def open(self):
        with allure.step('Open browser'):
            browser.open('')
            return self

    def search_python(self):
        with allure.step('Click search button'):
            browser.element('.header-right-menu__search').click()
        with allure.step('Input search word'):
            browser.element('[pikabu-role=search]').type('Python').press_enter()

    def successful_search_pyhton(self, data):
        browser.element('.stories-search-results').should(have.text(data.python))

    def search_by_filter_tag(self):
        with allure.step('Click filter tag'):
            browser.element('.stories-search__tags-group').click()
        with allure.step('Input search word'):
            browser.element('[pikabu-role=tag]').type('Мемы').press_enter()

    def check_search_by_filter_tag(self, data):
        browser.element('.stories-search__tags-wrapper').should(have.text(data.tag))
search_page = SearchPage()

