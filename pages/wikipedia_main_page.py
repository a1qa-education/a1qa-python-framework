from playwright.sync_api import Page
from framework.ui.elements.button import Button
from framework.ui.elements.dropdown import Dropdown
from framework.ui.elements.input import Input
from framework.ui.pages.base_page import BasePage

class WikipediaMainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Input(page, page.locator('input#searchInput'), 'main page unique element'), 'Main Page')
        self.search_language = Dropdown(page, page.locator('#searchLanguage'), 'Search language dropdown')
        self.search_text_box = Input(page, page.locator('//div[@class="search-input"]/input'), 'Search textbox')
        self.search_button = Button(page, page.locator('//form[@id="search-form"]/fieldset/button'), 'Search button')

    def select_english_language(self):
        self.search_language.select_option('English')

    def type_search_request(self, text: str):
        self.search_text_box.type_text(text)

    def search_click(self):
        self.search_button.click()
