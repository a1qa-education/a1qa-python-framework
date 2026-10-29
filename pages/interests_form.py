from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class InterestsForm(BasePage):
    def __init__(self, page: Page):
        unique_element = Button(page, "a[class*='avatar-and-interests']", "Interests form unique element")
        super().__init__(page, unique_element, "Interests Form")
        self._interests_title = Label(page, page.get_by_text("Choose 3 interests"), "Interests title")
        self._page_indicator = Label(page, "div.page-indicator", "Page indicator")

    def is_interests_title_displayed(self) -> bool:
        self._interests_title.state.wait_for_displayed(no_throw=True)
        return self._interests_title.state.is_displayed()

    def get_page_indicator_text(self) -> str:
        return self._page_indicator.get_text()
