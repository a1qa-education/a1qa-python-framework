from playwright.sync_api import Page

from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage
from pages.constants import MainPageNavigation


class MainPage(BasePage):
    """timeanddate.com home page."""

    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_text("Current Time", exact=True), "Main Page Header")
        super().__init__(page, unique_element, "Main Page")

    def _navigation_link(self, section: MainPageNavigation) -> Label:
        return Label(
            self.page,
            self.page.locator("#nav").get_by_role("listitem", name=section.value, exact=True),
            f"Navigation link: {section.value}"
        )

    def click_navigation_link(self, section: MainPageNavigation) -> None:
        """
        Opens a section from the main navigation menu.

        :param section: Navigation section to open.
        """
        self._navigation_link(section).click()
