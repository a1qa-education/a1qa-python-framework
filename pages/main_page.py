from playwright.sync_api import Page

from framework.ui.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h1:has-text("Welcome to the-internet")')
        super().__init__(page, header_locator, "Main Page")

        self._navigation_link = lambda text: self.page.get_by_text(text)

    def click_navigation_link(self, navigation_text):
        self._navigation_link(navigation_text).click()
