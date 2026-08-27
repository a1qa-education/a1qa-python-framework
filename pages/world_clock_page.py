import re

from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.input import Input
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class WorldClockPage(BasePage):
    """Personal World Clock page."""

    CITY_INPUT_ID = "addtxt"

    def __init__(self, page: Page):
        unique_element = Label(
            page,
            page.get_by_role("heading", name=re.compile("Personal World Clock", re.IGNORECASE)),
            "Personal World Clock Page unique element"
        )
        super().__init__(page, unique_element, "Personal World Clock")

        self.suggestion_items = page.locator('//ul[@class="asu"]//li/a')
        # Scoped to the Add City dialog: the page renders several modals.
        self.modal_title = Label(
            page,
            '//div[contains(@class,"modal-content")][.//input[@id="addtxt"]]'
            '//h2[contains(@class,"modal-title")]',
            "Modal title"
        )

    def personal_world_clock_button(self, text: str) -> Button:
        return Button(self.page, self.page.get_by_text(text), f"Personal World Clock Button: {text}")

    def personal_world_clock_modal(self, text: str) -> Label:
        return Label(
            self.page,
            f'//div[@class="modal-header"]/h2[text()="{text}"]',
            f"Personal World Clock Modal: {text}"
        )

    def modal_textbox(self, element_id: str) -> Input:
        return Input(self.page, f"#{element_id}", f"Modal Textbox with id: {element_id}")

    def modal_button(self, text: str) -> Button:
        return Button(
            self.page,
            self.page.locator("div.modal-footer").get_by_text(text),
            f"{text} Modal button"
        )

    def city_name_label(self, text: str) -> Label:
        return Label(self.page, f'//a[@class="c-city__name" and text()="{text}"]', "")

    def is_modal_opened(self, modal_name: str) -> None:
        assert self.personal_world_clock_modal(modal_name).state.is_displayed(), \
            f"Modal '{modal_name}' is not displayed"

    def get_modal_title_text(self) -> str:
        return self.modal_title.get_text().strip()

    def get_city_input_value(self) -> str:
        return self.modal_textbox(self.CITY_INPUT_ID).get_value()

    def get_city_name_text(self, text: str) -> str:
        return self.city_name_label(text).get_text().strip()

    def wait_for_suggestions_displayed(self, timeout: int) -> None:
        self.page.wait_for_timeout(timeout)

    def click_suggestion_item(self, number: int) -> None:
        self.suggestion_items.nth(number - 1).click()

    def click_modal_button(self, name: str) -> None:
        self.modal_button(name).click()
