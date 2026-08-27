import re

from playwright.sync_api import Page

from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class CityWeatherPage(BasePage):
    """Weather page of a single city."""

    def __init__(self, page: Page):
        unique_element = Label(
            page,
            page.get_by_role("heading", name=re.compile("Weather in", re.IGNORECASE)),
            "City Weather Page unique element"
        )
        super().__init__(page, unique_element, "City Weather Page")

        self.page_header = Label(page, '//h1[@class="headline-banner__title"]', "Page Header")

    def get_page_header_text(self) -> str:
        return self.page_header.get_text()
