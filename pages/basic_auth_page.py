from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class BasicAuthPage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("Basic Auth")')
        super().__init__(page, header_locator, "Basic Auth Page")

        self._auth_message = Label(page, "#content p", "Auth message")

    @step("Get authorization message")
    def get_auth_message(self) -> str:
        # Get message:
        pass
