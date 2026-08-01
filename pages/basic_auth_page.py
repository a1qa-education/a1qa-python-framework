from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class BasicAuthPage(BasePage):

    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_text("Basic Auth", exact=True), "Basic Auth Page Header")
        super().__init__(page, unique_element, "Basic Auth Page")

        self._auth_message = Label(page, "#content p", "Auth message")

    @step("Get authorization message")
    def get_auth_message(self) -> str:
        # Get message:
        pass
