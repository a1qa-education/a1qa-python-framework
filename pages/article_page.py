from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class ArticlePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Label(page, page.locator('//h1'), 'Article page unique element'), 'Article Page')
        self.page = page
        self.download_as_pdf_button = page.locator('a[title="Download this page as a PDF file"]')

    def click_tools_menu_button(self):
        self.page.locator('//div[@id="right-navigation"]//div[@class="vector-dropdown vector-page-tools-dropdown"]//input').click()

    def click_download_as_pdf_button(self):
        self.download_as_pdf_button.click()
