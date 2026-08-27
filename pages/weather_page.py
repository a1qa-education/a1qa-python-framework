from playwright.sync_api import Page

from framework.ui.constants.elements import ElementType
from framework.ui.elements.button import Button
from framework.ui.elements.elements_list import ElementsList
from framework.ui.elements.input import Input
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class WeatherPage(BasePage):
    """"Weather Around The World" search page."""

    def __init__(self, page: Page):
        unique_element = Label(
            page, page.get_by_role("heading", name="World Temperatures"), "Weather Page unique element"
        )
        super().__init__(page, unique_element, "Weather Page")

        self.search_input = Input(
            page,
            page.get_by_role("searchbox", name="Search for city, state or country…"),
            "Search textbox"
        )
        self.page_header_label = Label(page, "h1.bn-header__title", "Page Header")
        self.search_result_list = ElementsList(
            page, "ul.asu > li > a", "Search Results list", Button, ElementType.BUTTON
        )

    def check_page_title(self, expected: str) -> None:
        header_text = self.page_header_label.get_text()
        assert expected in header_text, f"Page header '{header_text}' does not contain '{expected}'"

    def wait_for_dropdown_apear(self, timeout: int) -> None:
        self.page.wait_for_timeout(timeout)

    def click_element_by_number(self, number: int) -> None:
        self.search_result_list.get_list_of_elements()[number - 1].click()
